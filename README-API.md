# 🏨 Hotel Booking API Testing Suite

A robust Postman API collection designed to validate end-to-end hotel booking workflows. This suite is structured as a technical portfolio piece demonstrating rigorous QA testing practices, comprehensive positive/negative test coverage, and automated token handling.

## 🛠️ Collection Structure & Test Coverage

This suite isolates test scenarios into structured folders to ensure comprehensive endpoint coverage:

### 🟢 Positive Flow (Happy Path)
Validates successful business operations and seamless data flow across sequential requests:
* **POST Auth:** Authenticates credentials and generates session tokens.
* **GET Booking Id Extraction:** Extracts and stores active IDs dynamically using variables.
* **GET GET Booking details:** Verifies precise data retrieval of existing reservation records.
* **POST Create Booking:** Tests new reservation generation with valid payloads.
* **PATCH Partial Update (PATCH):** Updates specific fields to confirm resource modification stability.

### 🔴 Negative Flow (Edge Cases & Error Handling)
Validates system resilience and precise HTTP error code responses under failure states:
* **POST Auth User error:** Verifies system handling of bad request payloads during login.
* **POST Auth 404:** Confirms resource not found routing behaviors.
* **DEL 403 invalid token:** Validates security measures and permission failures using malformed authorization.
