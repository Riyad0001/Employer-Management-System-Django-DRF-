download the repository and download all dependencies package.Then run migrate command and create superuser.
Run the project locally.For testing apis i used Talend API Tester.
where api end point use:
- `POST /api/auth/signup/`
- `POST /api/auth/login/`
- `GET /api/auth/profile/`
- `POST /api/employers/`
- `GET /api/employers/`
- `GET /api/employers/<id>/`
- `PUT /api/employers/<id>/`
- `DELETE /api/employers/<id>/`

Give methood with api and in header secton give:
Key: Authorization
Value: Bearer <access_token>
access_token get when you login browser /api/auth/login after signup

Then you get all employes Information
