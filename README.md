# pPLUKAN-FEB UI Biro Pendidikan Online

PPL Genap 2019/2020 Kelompok A6 dengan proyek FEB UI Biro Pendidikan Online

## Pipeline Status
[![pipeline status](https://gitlab.cs.ui.ac.id/ppl-fasilkom-ui/2020/pplukan-feb-ui-biro-pendidikan-online/badges/staging/pipeline.svg)](https://gitlab.cs.ui.ac.id/ppl-fasilkom-ui/2020/pplukan-feb-ui-biro-pendidikan-online/commits/staging)

## Coverage
[![coverage report](https://gitlab.cs.ui.ac.id/ppl-fasilkom-ui/2020/pplukan-feb-ui-biro-pendidikan-online/badges/staging/coverage.svg)](https://gitlab.cs.ui.ac.id/ppl-fasilkom-ui/2020/pplukan-feb-ui-biro-pendidikan-online/commits/staging)

## API Documentation:
http://birpen.docs.apiary.io/

## For development

### Installing dependencies

- Install dependencies for backend
  ```
  pip install -r requirements.txt
  pip install -r requirements_dev.txt
  ```

- Install dependencies for frontend
  ```
  npm install yarn
  yarn install
  ```
  
- Install postgresql
  ```
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  ```

- Set environment variable
  
  Create .env file based on .env.example
  ```
  cp birpen/.env.example birpen/.env
  ```
  
  Match variables' content in .env with your local environment settings

- Seed database
  ```
  bash seed.sh
  ```
  
### Testing

#### Testing for backend code

- Please read https://www.django-rest-framework.org/api-guide/testing/

- Run test
  ```
  coverage run --include='path/of/code/to/be/tested' manage.py test
  coverage report -m
  ```

#### Testing for frontend code

- Please read https://vue-test-utils.vuejs.org/guides/#writing-a-test and https://jestjs.io/docs/en/testing-frameworks
  
- Run test
  ```
  yarn test
  ```

### Start Development Server

#### Single Server
- Build static file from Vue.js
  ```
  yarn build
  ```
- Start Django development server
  ```
  python3 manage.py runserver
  ```

#### Dual server
- Start vue development server
  ```
  yarn serve
  ```
- Start Django development server
  ```
  python3 manage.py runserver
  ```

### Git Flow
To resolve each issue:  
- Create new branch "[username]/[issue's number]" from related PBI branch.
- Work on your branch
- After you finish your work, pull latest update from related PBI branch and resolve the conflict
- Push your work to your branch, make sure pipeline passed and no new issue at [sonarqube][1]   
- Create a new merge request to related PBI branch and mention the issue on the description.
- Mention at least two team member and ask for approval

For more information: http://bit.ly/GitFlowPPL

### Sonarqube Analysis
https://pmpl.cs.ui.ac.id/sonarqube/dashboard?id=ppl2020-a-feb_biro_pendidikan

[1]: https://pmpl.cs.ui.ac.id/sonarqube/dashboard?id=ppl2020-a-feb_biro_pendidikan