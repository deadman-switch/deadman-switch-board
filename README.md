# Deadman Switch Board

The Switch Board is where deadman switches are managed. Switches can be created programmatically via deadman-switch libraries. The Switch Board is also where API keys are created and managed for access.

On the Switch Board you can visualize all active switches and their status. The individual switches can be silenced or acknowledged from the web interface.


| Feature                | Implemented   
| -----------------------|:-------------:
| Teams and Users        | no
| API tokens management  | no
| Slack Integration      | no
| Email Integration      | no
| Pager Duty Integration | no
| Ops Gene Integration   | no

# Deadman Clients

Deadman clients are simple libraries implemented in common languages giving developers the ability to expose silent failures in their batch jobs, data processing routines, repeated functions, and cron processing behavior

| Feature                | Implemented   
| -----------------------|:-------------:
| Time based switch      | no
| S3 object switch       | no


### Time Based Switch

A time based deadman switch is implemented using EPOCH and a requested *frequency* at witch the time difference between last check-in and current time of which it can't exceed otherwise switch will be triggered. 

Example usage:

```python
import deadman
import os

deadman_token = os.environ['DEADMAN_TOKEN']

@deadman.switch(deadman_token, frequency="24hrs")
async def run_update_my_business_logic(req, resp, update):

```

### Progmatic Objects

* User
* Team
* Switch
* SwitchBoard
* Alert
