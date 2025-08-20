# Use ARM64 Apache image
FROM arm64v8/httpd:latest

# Remove default index.html
RUN rm /usr/local/apache2/htdocs/index.html

# Add custom index.html
COPY index.html /usr/local/apache2/htdocs/

# Expose port 80
EXPOSE 80

# Set working directory (optional)
WORKDIR /usr/local/apache2/htdocs/
