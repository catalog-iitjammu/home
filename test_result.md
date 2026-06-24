#====================================================================================================
# START - Testing Protocol - DO NOT EDIT OR REMOVE THIS SECTION
#====================================================================================================

# THIS SECTION CONTAINS CRITICAL TESTING INSTRUCTIONS FOR BOTH AGENTS
# BOTH MAIN_AGENT AND TESTING_AGENT MUST PRESERVE THIS ENTIRE BLOCK

# Communication Protocol:
# If the `testing_agent` is available, main agent should delegate all testing tasks to it.
#
# You have access to a file called `test_result.md`. This file contains the complete testing state
# and history, and is the primary means of communication between main and the testing agent.
#
# Main and testing agents must follow this exact format to maintain testing data. 
# The testing data must be entered in yaml format Below is the data structure:
# 
## user_problem_statement: {problem_statement}
## backend:
##   - task: "Task name"
##     implemented: true
##     working: true  # or false or "NA"
##     file: "file_path.py"
##     stuck_count: 0
##     priority: "high"  # or "medium" or "low"
##     needs_retesting: false
##     status_history:
##         -working: true  # or false or "NA"
##         -agent: "main"  # or "testing" or "user"
##         -comment: "Detailed comment about status"
##
## frontend:
##   - task: "Task name"
##     implemented: true
##     working: true  # or false or "NA"
##     file: "file_path.js"
##     stuck_count: 0
##     priority: "high"  # or "medium" or "low"
##     needs_retesting: false
##     status_history:
##         -working: true  # or false or "NA"
##         -agent: "main"  # or "testing" or "user"
##         -comment: "Detailed comment about status"
##
## metadata:
##   created_by: "main_agent"
##   version: "1.0"
##   test_sequence: 0
##   run_ui: false
##
## test_plan:
##   current_focus:
##     - "Task name 1"
##     - "Task name 2"
##   stuck_tasks:
##     - "Task name with persistent issues"
##   test_all: false
##   test_priority: "high_first"  # or "sequential" or "stuck_first"
##
## agent_communication:
##     -agent: "main"  # or "testing" or "user"
##     -message: "Communication message between agents"

# Protocol Guidelines for Main agent
#
# 1. Update Test Result File Before Testing:
#    - Main agent must always update the `test_result.md` file before calling the testing agent
#    - Add implementation details to the status_history
#    - Set `needs_retesting` to true for tasks that need testing
#    - Update the `test_plan` section to guide testing priorities
#    - Add a message to `agent_communication` explaining what you've done
#
# 2. Incorporate User Feedback:
#    - When a user provides feedback that something is or isn't working, add this information to the relevant task's status_history
#    - Update the working status based on user feedback
#    - If a user reports an issue with a task that was marked as working, increment the stuck_count
#    - Whenever user reports issue in the app, if we have testing agent and task_result.md file so find the appropriate task for that and append in status_history of that task to contain the user concern and problem as well 
#
# 3. Track Stuck Tasks:
#    - Monitor which tasks have high stuck_count values or where you are fixing same issue again and again, analyze that when you read task_result.md
#    - For persistent issues, use websearch tool to find solutions
#    - Pay special attention to tasks in the stuck_tasks list
#    - When you fix an issue with a stuck task, don't reset the stuck_count until the testing agent confirms it's working
#
# 4. Provide Context to Testing Agent:
#    - When calling the testing agent, provide clear instructions about:
#      - Which tasks need testing (reference the test_plan)
#      - Any authentication details or configuration needed
#      - Specific test scenarios to focus on
#      - Any known issues or edge cases to verify
#
# 5. Call the testing agent with specific instructions referring to test_result.md
#
# IMPORTANT: Main agent must ALWAYS update test_result.md BEFORE calling the testing agent, as it relies on this file to understand what to test next.

#====================================================================================================
# END - Testing Protocol - DO NOT EDIT OR REMOVE THIS SECTION
#====================================================================================================



#====================================================================================================
# Testing Data - Main Agent and testing sub agent both should log testing data below this section
#====================================================================================================

user_problem_statement: |
  Pixel-perfect clone of the Olin SmartCatalog layout, rebranded as "Indian Institute of Technology
  Jammu" (IIT Jammu). Multi-page catalog with sidebar tree navigation, breadcrumb, catalog version
  selector, search, Faculty pages, Academic Calendar, Fees and Financial Aid, Programs of Study,
  Courses-Credits-Hours by department, Academic Policies, and Table of Contents.

  User-reported bugs to verify after fix:
    1. Header logo / institute name should display cleanly with IIT Jammu logo image.
    2. Sidebar Search did not return results.
    3. Catalog version dropdown + "Select" button did not switch the catalog year.

backend:
  - task: "Catalog meta & navigation endpoints (/api/meta, /api/nav)"
    implemented: true
    working: true
    file: "backend/server.py"
    stuck_count: 0
    priority: "high"
    needs_retesting: false
    status_history:
        - working: "NA"
          agent: "main"
          comment: "GET /api/meta returns {versions, current}. GET /api/nav returns {tree:[...]}. Auto-seeds on first call."
        - working: true
          agent: "testing"
          comment: "✅ VERIFIED: GET /api/meta returns versions array (13 items) and current='Catalog 2024-25'. GET /api/nav returns tree with exactly 8 top-level nodes with correct slugs."

  - task: "Departments listing & detail (/api/departments, /api/departments/{slug})"
    implemented: true
    working: true
    file: "backend/server.py"
    stuck_count: 0
    priority: "high"
    needs_retesting: false
    status_history:
        - working: "NA"
          agent: "main"
          comment: "Lists 12 departments seeded from seed_data.py. Detail endpoint returns courses array."
        - working: true
          agent: "testing"
          comment: "✅ VERIFIED: GET /api/departments returns 12 departments. GET /api/departments/cse-computer-science-engineering returns CSE with 14 courses. 404 handling works correctly for non-existent slugs."

  - task: "Course add/remove on a department (/api/departments/{slug}/courses)"
    implemented: true
    working: true
    file: "backend/server.py"
    stuck_count: 0
    priority: "medium"
    needs_retesting: false
    status_history:
        - working: "NA"
          agent: "main"
          comment: "POST adds a course; duplicate code returns 409. DELETE removes by code; missing returns 404."
        - working: true
          agent: "testing"
          comment: "✅ VERIFIED: POST /api/departments/cse-computer-science-engineering/courses adds course successfully. Duplicate POST returns 409 Conflict. DELETE removes course. Second DELETE returns 404. All error handling correct."

  - task: "Faculty groups (/api/faculty, /api/faculty/{slug})"
    implemented: true
    working: true
    file: "backend/server.py"
    stuck_count: 0
    priority: "high"
    needs_retesting: false
    status_history:
        - working: "NA"
          agent: "main"
          comment: "5 faculty groups seeded (leadership, cse-faculty, ece-faculty, me-faculty, sciences-faculty)."
        - working: true
          agent: "testing"
          comment: "✅ VERIFIED: GET /api/faculty returns 5 faculty groups. GET /api/faculty/leadership returns 5 members. 404 handling works correctly for non-existent slugs."

  - task: "Academic Calendar (/api/calendar)"
    implemented: true
    working: true
    file: "backend/server.py"
    stuck_count: 0
    priority: "medium"
    needs_retesting: false
    status_history:
        - working: "NA"
          agent: "main"
          comment: "Returns Autumn + Spring 2024-25 terms with event/date rows."
        - working: true
          agent: "testing"
          comment: "✅ VERIFIED: GET /api/calendar returns 2 calendar terms (Autumn + Spring 2024-25)."

  - task: "Fees (/api/fees, /api/fees/{slug})"
    implemented: true
    working: true
    file: "backend/server.py"
    stuck_count: 0
    priority: "medium"
    needs_retesting: false
    status_history:
        - working: "NA"
          agent: "main"
          comment: "tuition-fees, hostel-mess, scholarships sections with tabular data."
        - working: true
          agent: "testing"
          comment: "✅ VERIFIED: GET /api/fees returns 3 fee sections. GET /api/fees/tuition-fees returns object with 2 tables. 404 handling works correctly for non-existent slugs."

  - task: "Info pages (/api/info-pages, /api/info-pages/{slug})"
    implemented: true
    working: true
    file: "backend/server.py"
    stuck_count: 0
    priority: "medium"
    needs_retesting: false
    status_history:
        - working: "NA"
          agent: "main"
          comment: "13 info pages for Information/Programs/Academic Policies sub-sections."
        - working: true
          agent: "testing"
          comment: "✅ VERIFIED: GET /api/info-pages returns 13 info pages. GET /api/info-pages/history returns 'History of IIT Jammu' with body array of 3 paragraphs. 404 handling works correctly for non-existent slugs."

  - task: "Search endpoint (/api/search)"
    implemented: true
    working: true
    file: "backend/server.py"
    stuck_count: 0
    priority: "high"
    needs_retesting: false
    status_history:
        - working: "NA"
          agent: "main"
          comment: "Search by q with scope=Entire Catalog | Programs | Courses. User reported sidebar search wasn't returning results; backend endpoint added with case-insensitive matching across sections, sub-pages, and course code/title/desc. Frontend SearchPage now calls /api/search and rewrites year segment in result URLs."
        - working: true
          agent: "testing"
          comment: "✅ VERIFIED: User-reported bug FIXED. GET /api/search?q=machine&scope=Courses returns CSL4010 Machine Learning. GET /api/search?q=programs&scope=Programs returns Section/Page results. GET /api/search?q=&scope=Entire Catalog returns 0 results gracefully. Case-insensitive matching works across sections, sub-pages, and course code/title/desc."

  - task: "Seed endpoint (/api/seed) + auto-seed on startup"
    implemented: true
    working: true
    file: "backend/server.py"
    stuck_count: 0
    priority: "high"
    needs_retesting: false
    status_history:
        - working: "NA"
          agent: "main"
          comment: "Idempotent upsert by slug; ?force=true wipes & reseeds. Auto-runs if departments collection empty."
        - working: true
          agent: "testing"
          comment: "✅ VERIFIED: POST /api/seed is idempotent (returns same counts on multiple calls). POST /api/seed?force=true wipes and reseeds with non-zero counts for all collections."

frontend:
  - task: "Header — IIT Jammu logo + full name (bold)"
    implemented: true
    working: "NA"
    file: "frontend/src/components/Header.jsx"
    stuck_count: 1
    priority: "medium"
    needs_retesting: false
    status_history:
        - working: "NA"
          agent: "main"
          comment: "Replaced SVG mock with the user-provided IIT Jammu logo image; full name now displayed in bold serif uppercase across two lines next to logo plus Devanagari tagline."

  - task: "Catalog version dropdown — actually switches catalog year"
    implemented: true
    working: "NA"
    file: "frontend/src/components/TopBar.jsx, frontend/src/App.js, frontend/src/context/CatalogContext.js"
    stuck_count: 1
    priority: "high"
    needs_retesting: false
    status_history:
        - working: "NA"
          agent: "main"
          comment: "Routes now use /en/:year/catalog dynamic param. Select button parses YYYY-YY from selected version and navigates to /en/{newYear}/catalog. All Link components in Sidebar, TopBar, pages now use useYear() hook."

  - task: "Sidebar search — wired to backend /api/search"
    implemented: true
    working: "NA"
    file: "frontend/src/components/Sidebar.jsx, frontend/src/pages/SearchPage.jsx, frontend/src/api/client.js"
    stuck_count: 1
    priority: "high"
    needs_retesting: false
    status_history:
        - working: "NA"
          agent: "main"
          comment: "Sidebar form navigates to /en/{year}/catalog/search?q=...&scope=...; SearchPage fetches /api/search and renders results with year-rewritten URLs."

metadata:
  created_by: "main_agent"
  version: "1.0"
  test_sequence: 1
  run_ui: false

test_plan:
  current_focus:
    - "Catalog meta & navigation endpoints (/api/meta, /api/nav)"
    - "Departments listing & detail (/api/departments, /api/departments/{slug})"
    - "Course add/remove on a department (/api/departments/{slug}/courses)"
    - "Faculty groups (/api/faculty, /api/faculty/{slug})"
    - "Academic Calendar (/api/calendar)"
    - "Fees (/api/fees, /api/fees/{slug})"
    - "Info pages (/api/info-pages, /api/info-pages/{slug})"
    - "Search endpoint (/api/search)"
    - "Seed endpoint (/api/seed) + auto-seed on startup"
  stuck_tasks: []
  test_all: false
  test_priority: "high_first"

agent_communication:
    - agent: "main"
      message: |
        Backend has been built with FastAPI + MongoDB and seeded with IIT Jammu catalog data
        (12 departments, 5 faculty groups, 2 calendar terms, 3 fee sections, 13 info pages,
        nav-tree, catalog versions list). All endpoints are under /api prefix.
        Frontend has been wired to the backend; pages call /api/* via axios client.
        Please verify all backend endpoints listed in test_plan. The user-reported search bug
        and catalog-version-switch bug have been fixed on the frontend, but the backend
        /api/search endpoint must be confirmed to return results for queries such as
        q="machine learning" (Entire Catalog), q="CSL" (Courses), q="faculty" (Programs).
        Confirm:
          - GET /api/ returns 200 with message.
          - GET /api/nav returns tree with 8 top-level nodes.
          - GET /api/meta returns versions array (>=10) and current="Catalog 2024-25".
          - GET /api/departments returns array of length 12.
          - GET /api/departments/cse-computer-science-engineering returns object with code "CSE" and 14 courses.
          - GET /api/faculty returns array of length 5; GET /api/faculty/leadership returns 5 members.
          - GET /api/calendar returns array of length 2.
          - GET /api/fees returns array of length 3; GET /api/fees/tuition-fees returns 2 tables.
          - GET /api/info-pages returns array of length 13; GET /api/info-pages/history returns "History of IIT Jammu" with 3 paragraphs.
          - GET /api/search?q=machine&scope=Courses returns >=1 course result; q=programs&scope=Programs returns >=1 section; q=&scope=Entire Catalog returns 0 results gracefully.
          - POST /api/departments/cse-computer-science-engineering/courses with new code adds; second POST same code -> 409; DELETE removes; DELETE same again -> 404.
          - POST /api/seed (no force) is idempotent; POST /api/seed?force=true wipes & reseeds.
    - agent: "testing"
      message: |
        ✅ BACKEND TESTING COMPLETE - ALL 22 TESTS PASSED
        
        Comprehensive backend API testing completed successfully. Created /app/backend_test.py
        and executed all tests against production backend URL (https://course-hours.preview.emergentagent.com/api).
        
        TEST RESULTS SUMMARY:
        • ✅ Root endpoint (/api/) - Returns 200 with IIT Jammu message
        • ✅ Meta endpoint (/api/meta) - Returns 13 catalog versions, current="Catalog 2024-25"
        • ✅ Nav endpoint (/api/nav) - Returns tree with 8 top-level nodes (all correct slugs)
        • ✅ Departments list (/api/departments) - Returns 12 departments
        • ✅ Departments detail (/api/departments/cse-computer-science-engineering) - Returns CSE with 14 courses
        • ✅ Course add/remove - POST adds, duplicate returns 409, DELETE removes, second DELETE returns 404
        • ✅ Faculty list (/api/faculty) - Returns 5 faculty groups
        • ✅ Faculty detail (/api/faculty/leadership) - Returns 5 members
        • ✅ Calendar (/api/calendar) - Returns 2 terms (Autumn + Spring 2024-25)
        • ✅ Fees list (/api/fees) - Returns 3 fee sections
        • ✅ Fees detail (/api/fees/tuition-fees) - Returns object with 2 tables
        • ✅ Info pages list (/api/info-pages) - Returns 13 info pages
        • ✅ Info pages detail (/api/info-pages/history) - Returns "History of IIT Jammu" with 3 paragraphs
        • ✅ Search - machine in Courses scope - Returns CSL4010 Machine Learning
        • ✅ Search - programs in Programs scope - Returns Section/Page results
        • ✅ Search - empty query - Returns 0 results gracefully
        • ✅ Seed idempotent - POST /api/seed returns same counts on multiple calls
        • ✅ Seed force - POST /api/seed?force=true wipes and reseeds with non-zero counts
        • ✅ 404 handling - All endpoints (departments, faculty, fees, info-pages) return 404 for non-existent slugs
        
        USER-REPORTED BUG VERIFICATION:
        ✅ Search bug FIXED: Backend /api/search endpoint returns results correctly for all test cases:
           - q=machine scope=Courses → Found CSL4010 Machine Learning
           - q=programs scope=Programs → Found Section/Page results
           - q= scope=Entire Catalog → Returns 0 results gracefully (no errors)
        
        All backend tasks marked as working: true, needs_retesting: false.
        No critical issues found. Backend is production-ready.
