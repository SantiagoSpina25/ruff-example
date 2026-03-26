FROM python:3.14.2-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# No default runtime behavior for this library-style project.
# Override CMD at runtime as needed.
CMD ["python", "-c", "print('Image built; provide your own command')"]
