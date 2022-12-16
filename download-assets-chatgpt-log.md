```
Can you write a python script that will given the github repository get download all release attachments of the latest release and will download them to a subdirectory? The repository url should be passed in as command line argument. Also all assets that end with zip should be extracted into a subdirectory with the name of the zip file.
```

```
I think you might want the github api url instead of the repository url as parameter? At least the result of the url is not json at the moment.
```

```
Instead of naming the local folder attachments, could you name him like the repository? Also could you check if the folder exists before you create it and in case it does exist remove it?
```

```
After the zip file are extracted can you delete them so they do not clutter up the directory?
```
