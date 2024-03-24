# mobile_worker

# .env Sample

This is a sample .env file for configuring your Django project. The .env file is used to store environment variables that your Django project needs for configuration.

## Environment Variables

- `DEBUG`: Set this to `1` to enable debugging mode. Debugging mode should only be enabled in development environments. Default is `0`.

- `HOST`: Specify the host IP address or domain name. Use `*` to listen on all available network interfaces.

- `PORT`: Specify the port number for the Django development server. Default is `8000`.

- `DATABASE_URL`: Specify the connection URL for your PostgreSQL database. Replace `username`, `password`, and `dbname` with your PostgreSQL credentials and database name.

- `SECRET_KEY`: Specify the secret key for your Django project. This key is used for cryptographic signing and should be kept secret. Replace `assdsad` with a secure random string.

## Sample .env File

```plaintext
DEBUG=1
HOST=*
PORT=8000
DATABASE_URL=postgres://username:password@localhost:5432/dbname
SECRET_KEY=assdsad
