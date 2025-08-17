# Use ARM64-compatible Apache base
FROM arm64v8/httpd:latest

# Remove default index.html (optional)
RUN rm /usr/local/apache2/htdocs/index.html

# Add custom index.html
ADD ./index.html /usr/local/apache2/htdocs/

# Expose port 80
EXPOSE 80
