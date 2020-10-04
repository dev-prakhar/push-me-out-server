# Push Me Out
Backend Server written in Python-Django for push me out

# Setup

### Secrets
* Create a new file in `push_me_out/push_me_out/secrets.py`
* Add following content in the file
```
APPLICATION_PRIVATE_KEY = {private_key_generated_while_setting_up_the_client}
VAPID_EMAIL = {your_email}
```

### Spinning Up the Server
* Run `make build_up`
* Create a superuser using `make superuser`
* Open `http://localhost:8001/admin` and login
