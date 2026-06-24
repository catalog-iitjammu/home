#!/usr/bin/env python3
"""
Comprehensive backend API test suite for IIT Jammu SmartCatalog.
Tests all endpoints with the production backend URL from frontend/.env
"""

import requests
import sys
import os
from pathlib import Path

# Read backend URL from frontend/.env
env_path = Path(__file__).parent / "frontend" / ".env"
BACKEND_URL = None
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            if line.startswith("REACT_APP_BACKEND_URL="):
                BACKEND_URL = line.split("=", 1)[1].strip()
                break

if not BACKEND_URL:
    print("❌ CRITICAL: Could not read REACT_APP_BACKEND_URL from frontend/.env")
    sys.exit(1)

BASE_URL = f"{BACKEND_URL}/api"
print(f"🔗 Testing backend at: {BASE_URL}\n")

# Test results tracking
passed = 0
failed = 0
test_results = []


def test(name, func):
    """Run a test and track results"""
    global passed, failed
    try:
        func()
        passed += 1
        test_results.append(("✅", name))
        print(f"✅ {name}")
    except AssertionError as e:
        failed += 1
        test_results.append(("❌", name, str(e)))
        print(f"❌ {name}")
        print(f"   Error: {e}")
    except Exception as e:
        failed += 1
        test_results.append(("❌", name, f"Exception: {e}"))
        print(f"❌ {name}")
        print(f"   Exception: {e}")


# ========== Test Functions ==========

def test_root():
    """GET /api/ returns 200 with message"""
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert "message" in data, "Response missing 'message' field"
    assert "IIT Jammu" in data["message"], f"Expected 'IIT Jammu' in message, got: {data['message']}"


def test_meta():
    """GET /api/meta returns versions array and current"""
    r = requests.get(f"{BASE_URL}/meta")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert "versions" in data, "Response missing 'versions' field"
    assert "current" in data, "Response missing 'current' field"
    assert isinstance(data["versions"], list), "versions should be a list"
    assert len(data["versions"]) >= 10, f"Expected >=10 versions, got {len(data['versions'])}"
    assert data["current"] == "Catalog 2024-25", f"Expected current='Catalog 2024-25', got '{data['current']}'"


def test_nav():
    """GET /api/nav returns tree with 8 top-level nodes"""
    r = requests.get(f"{BASE_URL}/nav")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert "tree" in data, "Response missing 'tree' field"
    tree = data["tree"]
    assert isinstance(tree, list), "tree should be a list"
    assert len(tree) == 8, f"Expected 8 top-level nodes, got {len(tree)}"
    # Verify expected slugs
    expected_slugs = [
        "information-about-iitjammu",
        "programs-of-study-and-degree-requirements",
        "courses-credits-hours",
        "faculty",
        "academic-calendar",
        "fees-and-financial-aid",
        "academic-policies-and-procedures",
        "table-of-contents",
    ]
    actual_slugs = [node["slug"] for node in tree]
    assert actual_slugs == expected_slugs, f"Nav tree slugs mismatch. Expected {expected_slugs}, got {actual_slugs}"


def test_departments_list():
    """GET /api/departments returns array of length 12"""
    r = requests.get(f"{BASE_URL}/departments")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert isinstance(data, list), "Response should be a list"
    assert len(data) == 12, f"Expected 12 departments, got {len(data)}"


def test_departments_detail():
    """GET /api/departments/cse-computer-science-engineering returns CSE with 14 courses"""
    r = requests.get(f"{BASE_URL}/departments/cse-computer-science-engineering")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert data["code"] == "CSE", f"Expected code='CSE', got '{data.get('code')}'"
    assert "courses" in data, "Response missing 'courses' field"
    assert len(data["courses"]) == 14, f"Expected 14 courses, got {len(data['courses'])}"


def test_departments_404():
    """GET /api/departments/non-existent-slug returns 404"""
    r = requests.get(f"{BASE_URL}/departments/non-existent-slug")
    assert r.status_code == 404, f"Expected 404, got {r.status_code}"


def test_course_add_remove():
    """POST/DELETE /api/departments/{slug}/courses - add, duplicate 409, remove, 404"""
    slug = "cse-computer-science-engineering"
    test_course = {
        "code": "CSL9999",
        "title": "Test Course",
        "credits": 3,
        "hours": "3-0-6",
        "desc": "Just for testing"
    }
    
    # Add course
    r = requests.post(f"{BASE_URL}/departments/{slug}/courses", json=test_course)
    assert r.status_code == 200, f"Expected 200 on add, got {r.status_code}"
    data = r.json()
    assert data.get("status") == "ok", f"Expected status='ok', got {data}"
    
    # Try to add same course again - should get 409
    r = requests.post(f"{BASE_URL}/departments/{slug}/courses", json=test_course)
    assert r.status_code == 409, f"Expected 409 on duplicate, got {r.status_code}"
    
    # Delete course
    r = requests.delete(f"{BASE_URL}/departments/{slug}/courses/CSL9999")
    assert r.status_code == 200, f"Expected 200 on delete, got {r.status_code}"
    data = r.json()
    assert data.get("status") == "ok", f"Expected status='ok', got {data}"
    
    # Try to delete again - should get 404
    r = requests.delete(f"{BASE_URL}/departments/{slug}/courses/CSL9999")
    assert r.status_code == 404, f"Expected 404 on second delete, got {r.status_code}"


def test_faculty_list():
    """GET /api/faculty returns array of length 5"""
    r = requests.get(f"{BASE_URL}/faculty")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert isinstance(data, list), "Response should be a list"
    assert len(data) == 5, f"Expected 5 faculty groups, got {len(data)}"


def test_faculty_detail():
    """GET /api/faculty/leadership returns 5 members"""
    r = requests.get(f"{BASE_URL}/faculty/leadership")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert "members" in data, "Response missing 'members' field"
    assert len(data["members"]) == 5, f"Expected 5 members, got {len(data['members'])}"


def test_faculty_404():
    """GET /api/faculty/nope returns 404"""
    r = requests.get(f"{BASE_URL}/faculty/nope")
    assert r.status_code == 404, f"Expected 404, got {r.status_code}"


def test_calendar():
    """GET /api/calendar returns array of length 2"""
    r = requests.get(f"{BASE_URL}/calendar")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert isinstance(data, list), "Response should be a list"
    assert len(data) == 2, f"Expected 2 calendar terms, got {len(data)}"


def test_fees_list():
    """GET /api/fees returns array of length 3"""
    r = requests.get(f"{BASE_URL}/fees")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert isinstance(data, list), "Response should be a list"
    assert len(data) == 3, f"Expected 3 fee sections, got {len(data)}"


def test_fees_detail():
    """GET /api/fees/tuition-fees returns object with 2 tables"""
    r = requests.get(f"{BASE_URL}/fees/tuition-fees")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert "tables" in data, "Response missing 'tables' field"
    assert len(data["tables"]) == 2, f"Expected 2 tables, got {len(data['tables'])}"


def test_fees_404():
    """GET /api/fees/nope returns 404"""
    r = requests.get(f"{BASE_URL}/fees/nope")
    assert r.status_code == 404, f"Expected 404, got {r.status_code}"


def test_info_pages_list():
    """GET /api/info-pages returns array of length 13"""
    r = requests.get(f"{BASE_URL}/info-pages")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert isinstance(data, list), "Response should be a list"
    assert len(data) == 13, f"Expected 13 info pages, got {len(data)}"


def test_info_pages_detail():
    """GET /api/info-pages/history returns 'History of IIT Jammu' with body array of length 3"""
    r = requests.get(f"{BASE_URL}/info-pages/history")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert data["title"] == "History of IIT Jammu", f"Expected title='History of IIT Jammu', got '{data.get('title')}'"
    assert "body" in data, "Response missing 'body' field"
    assert isinstance(data["body"], list), "body should be a list"
    assert len(data["body"]) == 3, f"Expected body array of length 3, got {len(data['body'])}"


def test_info_pages_404():
    """GET /api/info-pages/nope returns 404"""
    r = requests.get(f"{BASE_URL}/info-pages/nope")
    assert r.status_code == 404, f"Expected 404, got {r.status_code}"


def test_search_machine_courses():
    """GET /api/search?q=machine&scope=Courses returns >=1 result containing CSL4010 Machine Learning"""
    r = requests.get(f"{BASE_URL}/search", params={"q": "machine", "scope": "Courses"})
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert "results" in data, "Response missing 'results' field"
    assert len(data["results"]) >= 1, f"Expected >=1 result for 'machine', got {len(data['results'])}"
    # Check if CSL4010 Machine Learning is in results
    found_ml = False
    for result in data["results"]:
        if "CSL4010" in result.get("label", "") and "Machine Learning" in result.get("label", ""):
            found_ml = True
            break
    assert found_ml, f"Expected to find CSL4010 Machine Learning in results, got: {data['results']}"


def test_search_programs_scope():
    """GET /api/search?q=programs&scope=Programs returns >=1 Section/Page result"""
    r = requests.get(f"{BASE_URL}/search", params={"q": "programs", "scope": "Programs"})
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert "results" in data, "Response missing 'results' field"
    assert len(data["results"]) >= 1, f"Expected >=1 result for 'programs', got {len(data['results'])}"
    # Check that results are Section or Page type
    for result in data["results"]:
        assert result.get("type") in ["Section", "Page"], f"Expected Section/Page type, got {result.get('type')}"


def test_search_empty_query():
    """GET /api/search?q=&scope=Entire Catalog returns 0 results gracefully"""
    r = requests.get(f"{BASE_URL}/search", params={"q": "", "scope": "Entire Catalog"})
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert "results" in data, "Response missing 'results' field"
    assert len(data["results"]) == 0, f"Expected 0 results for empty query, got {len(data['results'])}"


def test_seed_idempotent():
    """POST /api/seed (no force) returns counts and is idempotent"""
    r = requests.post(f"{BASE_URL}/seed")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert data.get("status") == "ok", f"Expected status='ok', got {data}"
    assert "counts" in data, "Response missing 'counts' field"
    counts1 = data["counts"]
    
    # Call again - should be idempotent
    r = requests.post(f"{BASE_URL}/seed")
    assert r.status_code == 200, f"Expected 200 on second call, got {r.status_code}"
    data = r.json()
    counts2 = data["counts"]
    assert counts1 == counts2, f"Seed should be idempotent. First: {counts1}, Second: {counts2}"


def test_seed_force():
    """POST /api/seed?force=true wipes and reseeds (counts non-zero)"""
    r = requests.post(f"{BASE_URL}/seed", params={"force": "true"})
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert data.get("status") == "ok", f"Expected status='ok', got {data}"
    assert data.get("force") == True, f"Expected force=true, got {data.get('force')}"
    assert "counts" in data, "Response missing 'counts' field"
    counts = data["counts"]
    assert counts["departments"] > 0, f"Expected departments > 0, got {counts['departments']}"
    assert counts["faculty_groups"] > 0, f"Expected faculty_groups > 0, got {counts['faculty_groups']}"
    assert counts["calendar_terms"] > 0, f"Expected calendar_terms > 0, got {counts['calendar_terms']}"
    assert counts["fees"] > 0, f"Expected fees > 0, got {counts['fees']}"
    assert counts["info_pages"] > 0, f"Expected info_pages > 0, got {counts['info_pages']}"


# ========== Run All Tests ==========

print("=" * 70)
print("IIT JAMMU SMARTCATALOG BACKEND API TEST SUITE")
print("=" * 70)
print()

# High priority tests first
print("🔥 HIGH PRIORITY TESTS")
print("-" * 70)
test("Root endpoint", test_root)
test("Meta endpoint", test_meta)
test("Nav endpoint", test_nav)
test("Departments list", test_departments_list)
test("Departments detail", test_departments_detail)
test("Faculty list", test_faculty_list)
test("Faculty detail", test_faculty_detail)
test("Search - machine learning in Courses", test_search_machine_courses)
test("Search - programs in Programs scope", test_search_programs_scope)
test("Search - empty query", test_search_empty_query)
test("Seed idempotent", test_seed_idempotent)
test("Seed force", test_seed_force)

print()
print("📋 MEDIUM PRIORITY TESTS")
print("-" * 70)
test("Course add/remove", test_course_add_remove)
test("Calendar", test_calendar)
test("Fees list", test_fees_list)
test("Fees detail", test_fees_detail)
test("Info pages list", test_info_pages_list)
test("Info pages detail", test_info_pages_detail)

print()
print("🚫 404 ERROR HANDLING TESTS")
print("-" * 70)
test("Departments 404", test_departments_404)
test("Faculty 404", test_faculty_404)
test("Fees 404", test_fees_404)
test("Info pages 404", test_info_pages_404)

print()
print("=" * 70)
print("TEST SUMMARY")
print("=" * 70)
print(f"✅ Passed: {passed}")
print(f"❌ Failed: {failed}")
print(f"📊 Total:  {passed + failed}")
print()

if failed > 0:
    print("❌ FAILED TESTS:")
    for result in test_results:
        if result[0] == "❌":
            print(f"  • {result[1]}")
            if len(result) > 2:
                print(f"    {result[2]}")
    print()
    sys.exit(1)
else:
    print("🎉 ALL TESTS PASSED!")
    sys.exit(0)
