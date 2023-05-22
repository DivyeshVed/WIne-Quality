import pandas as pd
import matplotlib.pyplot as plt

#####################################
## READING RED AND WHITE WINE DATA ##
#####################################
redWineData = pd.read_csv("./data/winequality-red.csv")
whiteWineData = pd.read_csv("./data/winequality-white.csv")

######################################
## SUMMARY OF RED & WHITE WINE DATA ##
######################################
redSummary = redWineData.describe()
whiteSummary = whiteWineData.describe()
print(redSummary)

#####################################################
## SUMMARY OF THE QUALITY DATA OF RED & WHITE WINE ##
#####################################################
redQuality = redSummary["quality"]
whiteQuality = whiteSummary["quality"]

########################################################################################
## CREATING BAR CHARTS TO COMPARE THE MEANS OF ALL ATTRIUBUTES IN RED AND WHITE WINES ##
########################################################################################
plt.bar(redSummary.columns, redSummary.loc['mean'], label="Red Wine", color="red")
plt.xticks(rotation=45)
plt.xlabel("Attributes")
plt.ylabel("Mean value")
plt.title("Mean value of Attributes: Red Wine")
# plt.savefig("./figures/redWineAttributesMeans.jpeg")
plt.bar(whiteSummary.columns, whiteSummary.loc['mean'], label="White Wine", color="blue")
plt.xticks(rotation=45)
plt.xlabel("Attributes")
plt.ylabel("Mean value")
plt.title("Mean value of Attributes: White Wine")
# plt.savefig(("./figures/whiteWineAttributesMeans.jpeg"))




