# Auth Server

A Django-based authentication server for generating, validating, and checking access tokens via API endpoints.

## Features
- Generate unique access tokens
- Validate tokens and mark them as in use
- Check token status (active, in use, last used)
- Admin interface for managing tokens

## Project Structure
- `auth_server/` - Django project settings and configuration
- `auth_start/` - Main app for token management
- `staticfiles/` - Static assets for admin and other interfaces

## API Endpoints
- `POST /api/generate-token/` - Generate a new access token *(currently commented out in `urls.py`)*
- `GET /api/validate-token/?token=...` - Validate a token and mark as in use
- `GET /api/check-token/?token=...` - Check token status

## Models
- `AccessToken` - Stores token string, usage status, timestamps, and memo

## Admin
- Manage tokens via Django admin at `/admin/`

## Setup
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run migrations:
   ```sh
   python manage.py migrate
   ```
3. Start the server:
   ```sh
   python manage.py runserver
   ```

## Testing
- Add tests in `auth_start/tests.py` and run with:
  ```sh
  python manage.py test
  ```

## License
MIT
