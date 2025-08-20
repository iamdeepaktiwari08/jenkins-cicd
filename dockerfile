# Use ARM64-compatible Apache base
FROM arm64v8/httpd:latest

# Remove default index.html
RUN rm /usr/local/apache2/htdocs/index.html

# Add custom index.html
COPY index.html /usr/local/apache2/htdocs/

# Set working directory
WORKDIR /usr/local/apache2/htdocs/

# Expose port 80
EXPOSE 80

# Optional health check
HEALTHCHECK --interval=30s --timeout=5s CMD curl -f http://localhost/ || exit 1
