FROM python:3.9-alpine


WORKDIR /open_cart_test

COPY requirements.txt .

RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "--browser_name", "chrome", "--url", "https://demo.opencart.com"]
