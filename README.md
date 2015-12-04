# squirtle

### Team
* Stephanie Huang
* John Anukem
* Peter Jiang
* Jessica Xiang

### Environment Setup
To make sure everything runs properly on your machine, we suggest using vagrant. 
Once you have vagrant installed, you should type on your command line:

```
vagrant up
vagrant ssh
cd /vagrant
```

Update any new requirements you may need with:
```
pip install -r requirements.txt
```

Make sure all the app keys are loaded into your environment by running: 
`./setup.sh`. File is provided on the Slack channel.

Then to get the server up and running:
```
cd app
python app.py
```

Navigate to `localhost:5000` on your preferred browser to test things out!