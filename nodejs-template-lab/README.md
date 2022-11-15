# day8-templates

Edit the template using VI Editor:

1.	Login to the Openshift cluster at 
https://c100-e.us-east.containers.cloud.ibm.com:30596 

2.	Clone the day8-templates git repository
https://github.ibm.com/ocp-dev-bootcamp-2020-05/day8-templates.git 


3. Edit the todo-template.yaml for following changes in the VI editor:

    a.	MongoDB version should be set to 3.6
    
    b.	NodeJS version should be set to latest
    
    c.	Set default value of NPM Mirror to - https://registry.npmjs.org
    
    d.	Parameter DATABASE_NAME is required. 
    
    e. Git_URL is https://github.com/sclorg/nodejs-ex.git

4. Create a new app named “test-nodejs” using the updated template to your project namespace
   
5. Export the template from the deployed aapplication to “exported-template.yaml” and compare the same with the “todo-template.yaml” to understand the extra objects in the exported template.

6. Send the screen shot of the running app and email a copy of the two templates.

7. Cleanup the resources.