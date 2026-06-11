---
title: API Documentation Pattern
type: pattern
created: 2026-06-08
updated: 2026-06-11
lines: 274
status: active
---
# API Documentation Pattern

## Overview

This pattern provides a standardized approach to documenting APIs in AIgenta's code workspace. It ensures consistency, completeness, and clarity across all API documentation.

## Purpose

Use this pattern when documenting:
- RESTful APIs
- GraphQL APIs
- WebSocket APIs
- RPC APIs
- Internal or external APIs

## When to Use This Pattern

**Appropriate contexts:**
- Creating new API documentation
- Standardizing existing API docs
- Documenting third-party APIs for internal use
- Creating API reference guides
- Building integration documentation

**Not appropriate when:**
- Documenting simple function calls (use inline comments instead)
- Creating quick reference sheets (use cheat sheets)
- Documenting proprietary protocols without sharing (use internal docs)

## Essential Components

### 1. Overview Section
```markdown
# API Name

## Description
[Clear, concise description of what the API does]

## Purpose
[Why this API exists and what problems it solves]

## Audience
[Who uses this API: developers, partners, internal teams, etc.]

## Base URL
[Base URL for all endpoints, e.g., https://api.example.com/v1]

## Version
[Current version and versioning strategy]
```

### 2. Authentication Section
```markdown
## Authentication

### Required Authentication
[Type: API Key, OAuth2, JWT, Bearer Token, etc.]

### How to Authenticate
[Step-by-step instructions for obtaining and using credentials]

### Authentication Headers
[Example headers showing authentication format]

### Security Notes
[Any security considerations, rate limits, etc.]
```

### 3. Endpoints Section (Core)

For each endpoint:
```markdown
### GET /endpoint/path

**Description**: [What this endpoint does]

**Purpose**: [Why this endpoint exists, what use case it serves]

**Authentication**: [Required/Optional - which level]

**Parameters**:
- `param1` (required): Description
- `param2` (optional): Description

**Request Headers**:
- `Header-Name`: Value description

**Request Body**:
```json
{
  "field": "description",
  "field2": "description"
}
```

**Response Codes**:
- `200 OK`: Success
- `400 Bad Request`: Invalid input
- `401 Unauthorized`: Missing or invalid credentials
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

**Response Body** (200):
```json
{
  "field": "example value",
  "field2": "example value"
}
```

**Example Request**:
```bash
curl -X GET "https://api.example.com/v1/endpoint" \
  -H "Authorization: Bearer token"
```

**Example Response**:
```json
{
  "data": {...},
  "status": "success"
}
```

**Notes**:
- [Any special behavior, edge cases, or important details]
- [Rate limits, caching behavior, etc.]
```

### 4. Common Response Codes Section
```markdown
## Common Response Codes

| Code | Meaning | When Occurs |
|------|---------|-------------|
| 200 | OK | Successful request |
| 201 | Created | Resource created successfully |
| 204 | No Content | Successful request, no content returned |
| 400 | Bad Request | Invalid request parameters |
| 401 | Unauthorized | Missing or invalid authentication |
| 403 | Forbidden | Authenticated but not authorized |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Request conflicts with current state |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error |
| 503 | Service Unavailable | Service temporarily unavailable |
```

### 5. Data Models Section
```markdown
## Data Models

### ModelName
**Description**: [What this model represents]

**Fields**:
- `field1` (type): Description
- `field2` (type, optional): Description

**Example**:
```json
{
  "field1": "example",
  "field2": 123
}
```

**Validation Rules**:
- field1 must be...
- field2 must be between X and Y...
```

### 6. Error Handling Section
```markdown
## Error Handling

### Error Response Format
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {
      "field": "Specific error details"
    }
  }
}
```

### Common Error Codes
- `INVALID_PARAMS`: Request parameters are invalid
- `AUTH_FAILED`: Authentication failed
- `RATE_LIMITED`: Rate limit exceeded
- `RESOURCE_NOT_FOUND`: Requested resource doesn't exist

### Retry Strategy
[When and how to retry failed requests]
```

### 7. Rate Limits Section
```markdown
## Rate Limits

### Limits
- [Number] requests per [time period] per [scope]

### Headers
- `X-RateLimit-Limit`: Total limit
- `X-RateLimit-Remaining`: Requests remaining
- `X-RateLimit-Reset`: Unix timestamp of reset

### Behavior When Exceeded
- [What happens when limits are exceeded]
- [How long to wait before retrying]
```

### 8. SDKs and Tools Section
```markdown
## SDKs and Tools

### Official SDKs
- [Language]: [Link to SDK]
- [Language]: [Link to SDK]

### Community Tools
- [Tool Name]: [Description and link]
- [Tool Name]: [Description and link]

### Code Examples
[Language-specific examples for common operations]
```

### 9. Changelog Section
```markdown
## Changelog

### Version 2.0.0 (YYYY-MM-DD)
**Breaking Changes**:
- [Breaking change description]

**New Features**:
- [New feature description]

**Bug Fixes**:
- [Bug fix description]

### Version 1.0.0 (YYYY-MM-DD)
- Initial release
```

## Documentation Quality Standards

### Clarity
- Use simple, clear language
- Avoid jargon unless necessary
- Define technical terms
- Provide examples for complex concepts

### Completeness
- Document all endpoints
- Include all parameters and their types
- Cover all response codes
- Provide examples for major operations

### Consistency
- Use consistent terminology
- Follow consistent formatting
- Maintain consistent structure across endpoints
- Use consistent naming conventions

### Accuracy
- Keep documentation in sync with API
- Test examples before publishing
- Update documentation when API changes
- Document deprecations clearly

## Common Pitfalls to Avoid

### ❌ Missing Authentication Details
**Problem**: Not explaining how to authenticate
**Solution**: Always include authentication section with clear examples

### ❌ Incomplete Parameter Information
**Problem**: Not specifying required vs optional, types, or constraints
**Solution**: Document every parameter with type, required/optional, and constraints

### ❌ No Error Examples
**Problem**: Only showing success cases
**Solution**: Include error response examples and common error scenarios

### ❌ Outdated Examples
**Problem**: Example code doesn't work with current API
**Solution**: Test all examples regularly or automate example testing

### ❌ Missing Rate Limits
**Problem**: Not documenting rate limits
**Solution**: Always document rate limits and how to handle them

## Example Template Structure

```markdown
# [API Name] API Documentation

## Overview
[Description, purpose, audience]

## Quick Start
[5-minute getting started guide]

## Authentication
[Authentication details]

## Endpoints
### GET /endpoint
[Endpoint documentation]

### POST /endpoint
[Endpoint documentation]

## Data Models
[Model definitions]

## Error Handling
[Error codes and handling]

## Rate Limits
[Rate limit information]

## SDKs and Tools
[Official and community tools]

## Changelog
[Version history]

## Support
[Contact information, resources]
```

## Best Practices

1. **Start with Quick Start**: Give users a 5-minute guide to first success
2. **Provide Working Examples**: Every major operation should have a working example
3. **Document Errors**: Show what errors look like and how to handle them
4. **Keep It Updated**: API changes must be reflected in documentation immediately
5. **Get Feedback**: Regularly gather feedback from users about documentation quality
6. **Use Tools**: Consider API documentation tools (Swagger/OpenAPI, Postman, etc.)
7. **Version Your Docs**: Match documentation version to API version
8. **Include SDK Examples**: Show usage in multiple languages if applicable

## Integration with Other Patterns

- **README Template**: API overview in README
- **Architecture Documentation**: API in system architecture context
- **Integration Guide**: How to integrate with other systems

---

**Last Updated**: 2026-06-11
**Category**: Documentation Pattern
**Related Patterns**: readme-template.md, architecture-doc.md, integration-guide.md