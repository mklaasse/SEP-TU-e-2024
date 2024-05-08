# website

## Installation

### Prerequisites
1. Clone the repository.
2. Open the root folder.
3. Create a `.env` file in the root folder.
4. Add the following environment variables to the `.env` file:
``` properties
## Backend 
SECRET_KEY = "secret_key"
DB_NAME = "benchlab"
DB_HOST = "http://localhost:5432"
DB_USER = "user"
DB_PASSWORD = "password"

DEBUG = "True"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "some-smtp-ip.com"
EMAIL_FROM = "mymail@mail.com"
EMAIL_HOST_USER = "mymail@mail.com"
EMAIL_HOST_PASSWORD = "password"
EMAIL_PORT = "587"
EMAIL_USE_TLS = "True"

FRONTEND_URL = http://localhost:5173/

## Frontend 
VITE_API_URL = "http://localhost:8000/api"
```
<!-- 5. Create a virtual environment for the backend by running `virtualenv .venv` in the root folder. -->

### Frontend
1. Make sure you have **Node.js 20.13.0 LTS** installed on your machine. If not, please install it. **LINUX ONLY**: You might need to use Node Version Manager(NVM) to install this specific verison of Node.js. 
3. Install/Activate yarn (run `corepack enable`, this command might require admin priviliges).
4. Open the frontend folder.
5. Run `yarn` (this will install all dependencies).
6. To start vite you can run `yarn vite`.

### Backend
1. Make sure you have **Python 3.12.3** installed.
2. 

### Folder Structure
```
.root/
├─ .github/
├─ .venv/
├─ backend/
├─ docs/
├─ frontend/
├─ .env
├─ .gitignore
├─ README.md
├─ SECURITY.md
```


## !Use YARN to install dependencies for the frontend!


## Deployment
Use the production branch to deploy the webapp.


# Code quality analysis

## Usage

This worklfow is run whenever a commit is pushed to main or a pr into main is made. It may take between 1 to 3 minutes to complete the analysis. To view the results do the following:

Navigate to the github action and click on the job *Code Quality*:\
<img src="docs/github-action.jpg" width="500">

The *Show output* tab shows all the metrics gathered by the tools:\
<img src="docs/show-output.png" width="500">

The output starts with some intermediate debug results, which you can ignore.
The evaluation of you code is shown in the tables below. *Threshold violation percentages* is the percentage of files/code that violate the metrics shown in the table below. *Ranks* shows the combined rank for each maintainability attribute. It shows the grade that our code would get according to the metrics that the TU/e uses.


## Metrics

For each characteristic we compute what percentage of the code is above the threshold. Then a rank is computed for that characteristic. For each Maintainability attribute we compute the average rank (based on its corresponding code characteristics).

Code characteristic         | Metric                               | Threshold | Maintainability attr.
----------------------------|--------------------------------------|-----------|----------------------
Module size                 | SLOC                                 |  <=400    | ADT
Class complexity            | Cyclomatic per method: average; max  |  <10; <20 | DT
Class design (for OO)       | WMC                                  |  <=20     | MRAD
Module design (for non OO)  | Functions per module/file            |  <=20     | MRAD
Module internal duplication | % of duplicated SLOC inside modules  |  N/A      | RAD
Code commenting             | % LOCM                               |  >15%     | A
Cyclic dependencies         | # of between classes                 |  0        | MRADT
Module coupling             | CBO                                  |  <16      | MR
Module external duplication | % of duplicated SLOC between modules |  N/A      | MR

rank    |    % of modules/classes/packages above threshold
--------|-------------------------------------------------
+2      |    0-3%
+1      |    4-5%
0       |    6-10%
-1      |    11-20%
-2      |    21–100%

Code | Maintainability attribute
-----|--------------------------
M    | Modularity
R    | Reusability
A    | Analyzability
D    | Modifiability
T    | Testability

The code quality assessment document that TU/e uses can be found [here](https://canvas.tue.nl/courses/25283/files/folder/SEP%20Materials/Assessment%20and%20Guidelines?).


## Code analysis tools
TU/e uses [simian](http://www.harukizaemon.com/simian/index.html/) to analyse code duplication.
[understand](http://scitools.com/student) is used to derive all the other metrics.

**Note:** understand incorrectly computes Module coupling, it only accounts for classes in the same file. 
