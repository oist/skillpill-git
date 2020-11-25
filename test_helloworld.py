import HelloWorld

def test_mainNoArgs(capsys): #capsys is the capture of the sys stderr and stdout
    HelloWorld.callFctn(["test_helloworld.py"])
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"

def test_mainWithName(capsys):
    HelloWorld.callFctn(["test_helloworld.py", "Git User"])
    captured = capsys.readouterr()
    assert captured.out == "Hello Git User\n"

def test_mainWithNameAndTime_Morning(capsys):
    HelloWorld.callFctn(["test_helloworld.py", "Git User", "09:15"])
    captured = capsys.readouterr()
    assert captured.out == "Good morning Git User\n"

def test_mainWithNameAndTime_Afternoon(capsys):
    HelloWorld.callFctn(["test_helloworld.py", "Git User", "15:15"])
    captured = capsys.readouterr()
    assert captured.out == "Good afternoon Git User\n"

def test_mainWithNameAndTime_Evening(capsys):
    HelloWorld.callFctn(["test_helloworld.py", "Git User", "21:15"])
    captured = capsys.readouterr()
    assert captured.out == "Good evening Git User\n"