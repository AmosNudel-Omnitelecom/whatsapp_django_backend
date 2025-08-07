# WhatsApp Django Backend - Docker Deployment Guide

This guide provides instructions for deploying the WhatsApp Django backend using Docker and docker-compose.

## 📋 Prerequisites

- Docker installed on your system
- Docker Compose installed
- Git (for cloning the repository)

## 🚀 Quick Start Deployment

### 1. Clone and Setup

```bash
# Navigate to the project directory
cd /path/to/your/project

# Make the deployment script executable
chmod +x deploy.sh

# Run the deployment script
./deploy.sh
```

### 2. Manual Setup (Alternative)

#### Step 1: Environment Configuration

1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```

2. Edit the `.env` file with your actual values:
   ```bash
   nano .env
   ```

   Required variables:
   - `SECRET_KEY`: Django secret key
   - `DEBUG`: Set to `False` for production
   - `BUSINESS_PORTFOLIO_ID`: Your Facebook Business Portfolio ID
   - `ACCESS_TOKEN`: Your Facebook Access Token
   - `FACEBOOK_APP_ID`: Your Facebook App ID
   - `FACEBOOK_APP_SECRET`: Your Facebook App Secret
   - `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

#### Step 2: Build and Start Services

```bash
# Build the Docker images
docker-compose build

# Start all services in detached mode
docker-compose up -d
```

#### Step 3: Initialize Database

```bash
# Run database migrations
docker-compose exec web python manage.py migrate

# Create a superuser (optional)
docker-compose exec web python manage.py createsuperuser

# Collect static files
docker-compose exec web python manage.py collectstatic --noinput
```

## 🏗️ Architecture

The deployment includes the following services:

- **Web**: Django application running with Gunicorn
- **Nginx**: Reverse proxy and static file server
- **Redis**: For caching and session storage (optional)

### Port Mapping

- **Port 80**: Nginx (main application entry point)
- **Port 8000**: Django application (internal)
- **Port 6379**: Redis (internal)

## 🔧 Management Commands

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f web
docker-compose logs -f nginx
docker-compose logs -f redis
```

### Stop Services
```bash
docker-compose down
```

### Restart Services
```bash
docker-compose restart
```

### Update Application
```bash
# Pull latest changes
git pull

# Rebuild and restart
docker-compose down
docker-compose build
docker-compose up -d

# Run any new migrations
docker-compose exec web python manage.py migrate
```

### Access Application Shell
```bash
docker-compose exec web python manage.py shell
```

### Database Management
```bash
# Create new migration
docker-compose exec web python manage.py makemigrations

# Apply migrations
docker-compose exec web python manage.py migrate

# Load fixtures (if any)
docker-compose exec web python manage.py loaddata fixture_name
```

## 🔒 Security Considerations

### For Production Deployment:

1. **Environment Variables**: Ensure all sensitive variables are properly set in `.env`

2. **HTTPS**: Enable HTTPS by updating nginx configuration and uncommenting HTTPS-related settings in `settings.py`:
   ```python
   SECURE_SSL_REDIRECT = True
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   ```

3. **Domain Configuration**: Update `ALLOWED_HOSTS` in `.env` with your actual domain

4. **Firewall**: Configure firewall to only allow necessary ports (80, 443)

5. **Regular Updates**: Keep Docker images and dependencies updated

## 🗄️ Database

Currently using SQLite for simplicity. For production, consider:

1. **PostgreSQL Setup** (recommended for production):
   - Add PostgreSQL service to `docker-compose.yml`
   - Update `DATABASES` configuration in `settings.py`
   - Install `psycopg2` in `requirements.txt`

2. **Backup Strategy**:
   ```bash
   # SQLite backup
   docker-compose exec web python manage.py dumpdata > backup.json
   
   # Restore
   docker-compose exec web python manage.py loaddata backup.json
   ```

## 🔍 Troubleshooting

### Common Issues:

1. **Permission Errors**:
   ```bash
   sudo chown -R $USER:$USER .
   ```

2. **Port Already in Use**:
   ```bash
   # Check what's using the port
   sudo lsof -i :80
   
   # Stop the process or change port in docker-compose.yml
   ```

3. **Static Files Not Loading**:
   ```bash
   docker-compose exec web python manage.py collectstatic --clear --noinput
   ```

4. **Database Connection Issues**:
   - Ensure SQLite file permissions are correct
   - Check volume mounts in docker-compose.yml

### Debug Mode:

To enable debug mode temporarily:
```bash
# Edit .env file
DEBUG=True

# Restart services
docker-compose restart
```

## 📊 Monitoring

### Application Health Check:
```bash
curl http://localhost/admin/
```

### Resource Usage:
```bash
docker stats
```

### Container Status:
```bash
docker-compose ps
```

## 🎯 Next Steps

1. Set up SSL certificates (Let's Encrypt recommended)
2. Configure domain name and DNS
3. Set up monitoring and logging
4. Implement backup strategy
5. Configure CI/CD pipeline

## 📞 Support

For issues related to:
- Django application: Check application logs
- Docker deployment: Check container logs
- Facebook API: Verify API credentials and permissions

Remember to never commit sensitive information like API keys or secrets to version control.
