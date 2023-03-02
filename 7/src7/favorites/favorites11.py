# Searches database popularity of a problem

import csv

from cs50 import SQL

# Open database
db = SQL("sqlite:///favorites.db")   #industry-wide syntax (not only cs50 thing)
                                     #which is telling to open fav.db file using sqlite3 technology
# Prompt user for favorite
favorite = input("Favorite: ")

# Search for title
rows = db.execute("SELECT COUNT(*) FROM favorites WHERE problem LIKE ?", "%" + favorite + "%")
         #cool cs50 function                                         #placeholder



#############  RACE CONDITION #####################################

        #rows = db.execute("SELECT likes FROM posts WHERE id = ?", id);
        #likes = rows[0]["likes"]
        #db.execute ("UPDATE posts SET likes = ? WHERE id =?", likes + 1, id);

########################################################################


# Get first (and only) row
row = rows[0]

# Print popularity
print(row["COUNT(*)"])
