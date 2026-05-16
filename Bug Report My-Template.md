# Bug Report Template

---

## 1. Summary
*One sentence describing what is broken and where (e.g., "API ignores query parameter and returns unfiltered results").*

---

## 2. Description
*2–3 sentences explaining the bug clearly — what is broken, at which layer (frontend/backend/API/database)*

---

## 3. Steps to Replicate

1. **Login:** Access the system as **[User Role — e.g., Business Account / Admin]**
2. **Navigate:** Go to **[Section or Page]**
3. **Pre-requisite:** Ensure **[any data or setup required]**
4. **Action:** **[Exact action the user performs]**
5. **Observe:** Check **[where to look — UI, Network tab, console, etc.]**

---

## 4. API Evidence *(if applicable)*

| Property | Value |
|----------|-------|
| **URL** | `https://example.com/api/v1/endpoint?param=value` |
| **Method** | `GET` / `POST` / `PUT` / `DELETE` |
| **Status Code** | `200 OK` / `400 Bad Request` / etc. |
| **Auth** | Bearer token / API Key / None |

**Actual Response Body:**
```json
{
  "count": 10,
  "results": [ ... all records returned, unfiltered ... ]
}
```

**Expected Response Body:**
```json
{
  "count": 1,
  "results": [ ... only matching records ... ]
}
```

---

## 5. Severity & Priority

| Property | Value |
|----------|-------|
| **Severity** | Critical / High / Medium / Low |
| **Priority** | P1 / P2 / P3 / P4 |
| **Type** | Functional / Performance / UI / API / Security |

---

## 6. Environment

| Property | Value |
|----------|-------|
| **Environment** | Dev / Staging (UAT) / Production |
| **Build / Version** | v1.x.x or Sprint name |
| **Browser** | Chrome 124 / Firefox 125 |
| **OS** | Windows 11 / macOS |

---

## 7. Test Data

| Field | Value |
|-------|-------|
| **Username** | testuser@yopmail.com |
| **Password** | Test@123 |
| **Account Type** | Business / Admin / Standard |

---

## 8. Attachments

- [ ] Screenshot
- [ ] Screen recording
- [ ] Network request/response logs
- [ ] Console errors

---

## 9. Additional Notes if any
