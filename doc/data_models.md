
#### Submission request data

```json
{
  "target_id": "<USER ID HERE>",
  "timestamp": "<TIMESTAMP IN SECONDS HERE>",
  "action_type": "ActionTYpe.<ACTION_TYPE>.value",
  "action_info": "<additional useful info  about action; e.g: what is changed selection or which trial is submitted>"
}
```

* `target_id` is `team_id` or `user_id`

#### Submission response data

`HTTP 200 OK` or `HTTP 400 bad request`


#### Query request data

* all fields are __optional__.
```json
{
  "filter_criteria": "<JSON_FILTER_CRITERIA>",
  "projection": "<JSON_PROJECTION>",
  "skip": "<number of results to skip>",
  "limit": "<number of results to return>"
}
```

