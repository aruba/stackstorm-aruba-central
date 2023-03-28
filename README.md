# Aruba Central Integration Pack
This pack allows you to integrate stackstorm with Aruba Central

## Configuration
Copy the example configuration in [arubacentral.yaml.example](./arubacentral.yaml.example) to
`/opt/stackstorm/configs/arubacentral.yaml` and edit as required.

It must contain:

```
base_url - The URL address for the aruba central account
username - User name
password - Password
client_id - client ID from arubacentral
client_secret - client_secret from arubacentral
customer_id - from arubacentral

```

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

Example configuration:

```yaml
---
  base_url: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  client_id: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  client_secret: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  customer_id: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  username: "me@me.com"
  password: "Ch@ng3Me!"
```
You can also run `st2 pack config arubacentral` and answer the prompts

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`


## Actions

Actions are defined in two groups:

### Individual actions: GET, POST, PUT with under bar will precede each individual action
* ``get_groups``
* ``post_groups``

### Orquestra Workflows: will not use underscore, dashes are used in the filename.


### To get this pack to work with A SINGLE HOST DEPLOYMENT StackStorm mongo DB
You can ignore this section when using StackStorm in docker containers. There is
no username and password associated with the database running in the mongo container.
Use at your own discretion.

```
docker pull stackstorm/stackstorm
```
