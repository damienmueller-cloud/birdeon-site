# Birdeon preview site

Static visual preview for birdeon.com. Plain HTML/CSS and a little JavaScript. No backend, no prices, no cart, no checkout.

Forms (notify me, contact) are visual only and do not send or store data.

## Preview locally

```bash
python3 -m http.server 8877 --bind 127.0.0.1
```

Then open http://127.0.0.1:8877/

Do not deploy or change DNS from this folder without review. The site is built to be portable to Shopify later.

Regenerate pages after editing product copy:

```bash
python3 build.py
```
