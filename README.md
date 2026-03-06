# Ecommerce-Gemini

Sprint 1 usually focuses on building the **Minimum Viable Product (MVP)** or a "Walking Skeleton"—the foundational features that allow a user to complete the most basic, core journey. For an e-commerce platform, the absolute core journey is: **Arriving at the site -> Finding a product -> Viewing the product -> Creating an account/Logging in**.

### Deployment Instructions

1. Open your terminal and navigate to the `sprint1-prototype` directory.
2. Run the following command to build the images and start the containers:
```bash
docker-compose up --build -d

```


3. Open your browser and go to `http://localhost`. You will see the Vue.js frontend served by Nginx, fetching product data directly from the FastAPI backend.
