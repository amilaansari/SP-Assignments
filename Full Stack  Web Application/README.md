# Development Process

## Starting a feature 

1. Checkout to master 

  ```
  git checkout master
  ```
  
2. Sync your local master with `origin/master`

  ```
  git pull
  ```
  
3. Create a new branch (Branch name format: `<YOUR_NAME>/feature/<FEATURE_NAME>`)

  ```
  git checkout -b jeremiah-ang/feature/magical-feature
  ```
  
## Development

4. Make changes, stage and commit

  ```
  git add <FILE_NAME>
  git commit -m "Meaningful message"
  ```
  
## Merging into master

5. Checkout to master and sync with origin/master

  ```
  git checkout master
  git pull
  ```
  
6. Checkout to feature branch again and merge master into feature branch.

  ```
  git checkout jeremiah-ang/feature/magical-feature
  git merge master
  ```
  
7. Resolve any merge conflict, test and commit the resolved merge conflict.

  ```
  git add <FILE_NAME>
  git commit -m "Merge master into jeremiah-ang/feature/magical-feature"
  ```

8. Push feature branch to origin

  ```
  git push origin jeremiah-ang/feature/magical-feature
  ```
 
9. Open a pull request
10. If the team is agree-able with the changes, merge into master. 
11. Repeat `step 1` again for the next feature. 
