# Github automation

This script automates git operations such as : 

* Create basic/data science repository
* Delete repository local/remote
* Add Colaborators 
* Print list of user repositories 

## Getting Started 

### Install: 

```bash
git clone "https://github.com/MikeG27/github_automation.git"
cd Github-automation
pip install -r requirements.txt

Then go to config.py and set : 
 * username,
 * password,
 * repository path,
 * colaborators[optional].
```

### Usage:
```bash
To run the script type in 'python git_manager -n "repo_name" -op <operation>'
```

### Operation types :
```bash
 1. Create normal repository - create
 2. Create Data Science repository - create_ds
 3. Detete repository - delete
 4. Print user repositories - print
 ```
