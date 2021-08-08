kaggle datasets download -d raghavramasamy/crop-statistics-fao-all-countries -p $HOME
unzip $HOME/crop-statistics-fao-all-countries.zip -d $HOME
sed -i 's/é/e/g' $HOME/Crops_AllData_Normalized.csv
