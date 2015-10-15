typo: ready
	@- git add --all .	
	@- git status
	@- git commit -am "commit with a makefile"
	@- git push origin master # <== update as needed

commit: ready 
	@- git status
	@- git commit -a
	@- git push origin master

update: ready
	@- git pull origin master

status: ready
	@- git status

ready: ready
	@git config --global credential.helper cache
	@git config credential.helper 'cache --timeout=3600'

rahlk:  # <== change to your name
	@git config --global user.name "rahlk"
	@git config --global user.email i.m.ralk@gmail.com