SAP Lumira Data Access Extension for Presto
===========================
By [Michal Korzen](http://scn.sap.com/people/michal.korzen)
Originally by [Alper Derici](http://scn.sap.com/people/alper.derici%40sap)

A Lumira Data Access Extension to fetch data from Presto

<strong>Installation: Activate Data Source Extensions in Lumira</strong> <br>
1. Go to the directory where SAP Lumira is installed: C:\Program Files\SAP Lumira\Desktop <br>
2. Create a folder called daextensions in the C:\Program Files\SAP Lumira\Desktop directory and open SAPLumira.ini file with a text editor. <br>
![Catalog](images/a.jpg?raw=true "Catalog")<br>
3. Add the following lines of code to the SAPLumira.ini file: <br>
  -Dhilo.externalds.folder=C:\Program Files\SAP Lumira\Desktop\daextensions <br>
  -Dactivate.externaldatasource.ds=true <br>
![inifile](images/b.jpg?raw=true "inifile")<br>
4. Download the executable file called [Presto.exe](bin/Presto.exe?raw=true "Presto.exe") to the directory we just created.<br>

<strong>Use: Import data extension into Lumira</strong> <br>
1. Now open up Lumira and add a new dataset from an external data source, we can see the Presto as an uncategorized extension:<br>
![dataset](images/d.jpg?raw=true "dataset")<br>
2. Provide extraction parameters<br>
![params](images/e.jpg?raw=true "params")<br>
3. Get live insights</strong> <br>
![insight](images/f.jpg?raw=true "insight")<br>
