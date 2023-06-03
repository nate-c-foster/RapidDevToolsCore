
import shutil
import os



#*****************************************************************************************************
# Author:         Nate Foster
# Company:        A.W. Schultz
# Date:           March 2023
#*****************************************************************************************************	
def createTempDirectory(directoryName):
	"""Creates a temporary directory.
	"""

	tempLocation = settings.getValue('Global','serverTempSaveLocation')
	path = tempLocation + '/' + directoryName

	os.mkdir(path)



#*****************************************************************************************************
# Author:         Nate Foster
# Company:        A.W. Schultz
# Date:           March 2023
#*****************************************************************************************************	
def zipTempDirectory(directoryName):
	"""Zip temporary directory.
	"""

	tempLocation = settings.getValue('Global','serverTempSaveLocation')
	path = tempLocation + '/' + directoryName


	shutil.make_archive(path, 'zip', path)
	shutil.rmtree(path)
	
	
	
	
#*****************************************************************************************************
# Author:         Nate Foster
# Company:        A.W. Schultz
# Date:           March 2023
#*****************************************************************************************************	
def copyToTempDirectory(sourcePath, directoryName):	
	"""Copy file/folder from sourcePath to temporary directoryName
	"""
	tempLocation = settings.getValue('Global','serverTempSaveLocation')
	destinationPath = tempLocation + '/' + directoryName
	
	if os.path.isfile(sourcePath):
		shutil.copy(sourcePath, destinationPath)
	elif os.path.isdir(sourcePath):
		shutil.copytree(sourcePath, destinationPath)
	else:
		print 'Error: Not a file or folder'
	
	
	

#*****************************************************************************************************
# Author:         Nate Foster
# Company:        A.W. Schultz
# Date:           March 2023
#*****************************************************************************************************		
def downloadTempFile(fileName):
	"""Transfer temporary file from gateway computer to session computer downloads folder
	"""

	tempLocation = settings.getValue('Global','serverTempSaveLocation')
	path = tempLocation + '/' + fileName

	importReadBytes = system.file.readFileAsBytes(path)
	system.perspective.download(fileName,importReadBytes)
	




#*****************************************************************************************************
# Author:         Nate Foster
# Company:        A.W. Schultz
# Date:           March 2023
#*****************************************************************************************************		
def getProjectNames():
	"""Get a list of non-default project names
	"""

	installationPath = settings.getValue('Global', 'installationPathIA')
	projectsPath = installationPath + '/Ignition/data/projects'
	
	dirList = os.listdir(projectsPath)
	
	
	defaultProjects = ['samplequickstart']
	projects = []
	for name in dirList:
		if name not in defaultProjects and '.' not in name:
			projects.append(name)
			
	return projects


#*****************************************************************************************************
# Author:         Nate Foster
# Company:        A.W. Schultz
# Date:           March 2023
#*****************************************************************************************************	
def getTagProviders():
	"""Get a list of tag providers.
	"""
	
	tags = system.tag.browse('')
	tagProviders = []
	for tag in tags:
		tagProviders.append(tag['fullPath'])
		
	return tagProviders
		


#*****************************************************************************************************
# Author:         Nate Foster
# Company:        A.W. Schultz
# Date:           March 2023
#*****************************************************************************************************			
def getThemeNames():
	"""Get a list of non-default theme names
	"""

	installationPath = settings.getValue('Global','installationPathIA')
	themesPath = installationPath + '/Ignition/data/modules/com.inductiveautomation.perspective/themes'
	
	dirList = os.listdir(themesPath)
	
	defaultThemes = ['dark','dark-cool','dark-warm','light','light-cool','light-warm','light-cool']
	themes = []
	for name in dirList:
		if name not in defaultThemes and '.' not in name:
			themes.append(name)

	return themes
	

#*****************************************************************************************************
# Author:         Nate Foster
# Company:        A.W. Schultz
# Date:           March 2023
#*****************************************************************************************************			
def exportTags(fileName, tagPath):
	"""Export tags
	"""
	filePath = settings.getValue('Global','serverTempSaveLocation') + '/' + fileName
	system.tag.exportTags(filePath, [tagPath], True)	
	



#*****************************************************************************************************
# Author:         Nate Foster
# Company:        A.W. Schultz
# Date:           June 2023
#*****************************************************************************************************		
def copyFileToProject(sourceSuffixPath,  destSuffixPath, projectName):
	"""Copy file from the temp folder to the project resource folder.
	
	Args:
		sourceSuffixPath (str): The suffix path within the temp folder. Does not start with '/'.
		destSuffixPath (str): The suffix path within the project resources folder. Does not start with '/'.
		projectName (str): The project name where the resources will be copied to

	"""

	tempLocation = settings.getValue('Global','serverTempSaveLocation')
	sourcePath = tempLocation + '/' + sourceSuffixPath
	
	installationPath = settings.getValue('Global','installationPathIA')
	destinationPath = installationPath + '/Ignition/data/projects/' + projectName + '/resources/' + destSuffixPath
	
#	print 'source : ', sourcePath
#	print 'destination : ', destinationPath
	
	fileBytes = system.file.readFileAsBytes(sourcePath)
	system.file.writeFile(destinationPath,fileBytes)
	
	
#*****************************************************************************************************
# Author:         Nate Foster
# Company:        A.W. Schultz
# Date:           June 2023
#*****************************************************************************************************	
def copyFolderToProject(sourceSuffixPath, destSuffixPath, projectName):
	"""Copy folder from the temp folder to the project resource folder.
	
	Args:
		sourceSuffixPath (str): The suffix path within the temp folder. Does not start with '/'.
		destSuffixPath (str): The suffix path within the project resources folder. Does not start with '/'.
		projectName (str): The project name where the resources will be copied to

	"""

	tempLocation = settings.getValue('Global','serverTempSaveLocation')
	fullSourcePath = tempLocation + '/' + sourceSuffixPath
	
	for dirpath, dirnames, filenames in os.walk(fullSourcePath):

		for fileName in filenames:
			fileSuffixPath = dirpath[len(fullSourcePath):].replace('\\','/') + '/' + fileName
			sourcePath = sourceSuffixPath + fileSuffixPath
			destPath = destSuffixPath +  fileSuffixPath
	
			copyFileToProject(sourcePath, destPath, projectName)

	

	
	
	
	
	
	
	
