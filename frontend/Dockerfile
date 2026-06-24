# Frontend Dockerfile — React (CRA + craco) dev server for local use
FROM node:20-alpine

WORKDIR /app

# Install yarn deps first for caching
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

# Copy source
COPY . .

EXPOSE 3000

# CRA dev server. For a production build use `yarn build` and serve with nginx.
CMD ["yarn", "start"]
