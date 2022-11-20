# django-2021

## test project for ANSWER
- create basic project by django
- publish to github
- publish to heroku

## demo on heroku
- home -> https://answerdemo.herokuapp.com/
- admin -> https://answerdemo.herokuapp.com/admin/

## 需求訪談
- 班別要有大分類 : 常態班(雙月收), 美語班(一期收), 寒暑假班
- 繳費時要能拆單 : clone 原繳費單, 原金額分散到兩份繳費單
- 教材費的特殊處理 : 只有第一期需要

## move to render
- ref https://render.com/docs/deploy-django
- 改用 poetry 代替 pipenv
- create build.sh, render.yaml
- poetry init
- poetry add Django
- poetry add :
  - django-debug-toolbar
  - django-jazzmin
  - django-adminlte-3
  - dj-database-url
  - gunicorn
  - whitenoise[brotli]

