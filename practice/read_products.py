{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9aceafea",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'C:\\\\Users\\\\anushka.makode\\\\DE-Bootcamp\\\\practice\\\\products.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 6\u001b[39m\n\u001b[32m      3\u001b[39m products = []  \u001b[38;5;66;03m# Empty list to store processed data\u001b[39;00m\n\u001b[32m      5\u001b[39m \u001b[38;5;66;03m# Open the CSV file using the full correct path\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m6\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[33;43mr\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mC:\u001b[39;49m\u001b[33;43m\\\u001b[39;49m\u001b[33;43mUsers\u001b[39;49m\u001b[33;43m\\\u001b[39;49m\u001b[33;43manushka.makode\u001b[39;49m\u001b[33;43m\\\u001b[39;49m\u001b[33;43mDE-Bootcamp\u001b[39;49m\u001b[33;43m\\\u001b[39;49m\u001b[33;43mpractice\u001b[39;49m\u001b[33;43m\\\u001b[39;49m\u001b[33;43mproducts.csv\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mmode\u001b[49m\u001b[43m=\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mr\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m=\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mutf-8\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m file:\n\u001b[32m      7\u001b[39m     reader = csv.DictReader(file)  \u001b[38;5;66;03m# Reads CSV as dictionary instead of list\u001b[39;00m\n\u001b[32m      9\u001b[39m     \u001b[38;5;28;01mfor\u001b[39;00m row \u001b[38;5;129;01min\u001b[39;00m reader:\n\u001b[32m     10\u001b[39m         \u001b[38;5;66;03m# Convert some fields to correct data types\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\IPython\\core\\interactiveshell.py:343\u001b[39m, in \u001b[36m_modified_open\u001b[39m\u001b[34m(file, *args, **kwargs)\u001b[39m\n\u001b[32m    336\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[32m0\u001b[39m, \u001b[32m1\u001b[39m, \u001b[32m2\u001b[39m}:\n\u001b[32m    337\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[32m    338\u001b[39m         \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mIPython won\u001b[39m\u001b[33m'\u001b[39m\u001b[33mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m by default \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    339\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    340\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33myou can use builtins\u001b[39m\u001b[33m'\u001b[39m\u001b[33m open.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    341\u001b[39m     )\n\u001b[32m--> \u001b[39m\u001b[32m343\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mio_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] No such file or directory: 'C:\\\\Users\\\\anushka.makode\\\\DE-Bootcamp\\\\practice\\\\products.csv'"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "\n",
    "products = []  # Empty list to store processed data\n",
    "\n",
    "# Open the CSV file using the full correct path\n",
    "with open(r\"C:\\Users\\anushka.makode\\DE-Bootcamp\\practice\\products.csv\", mode=\"r\", encoding=\"utf-8\") as file:\n",
    "    reader = csv.DictReader(file)  # Reads CSV as dictionary instead of list\n",
    "\n",
    "    for row in reader:\n",
    "        # Convert some fields to correct data types\n",
    "        row[\"Price\"] = float(row[\"Price\"])\n",
    "        row[\"Stock\"] = int(row[\"Stock\"])\n",
    "        row[\"Rating\"] = float(row[\"Rating\"])\n",
    "        products.append(row)\n",
    "\n",
    "print(\"Total products read:\", len(products))\n",
    "print(\"Example record:\", products[0])\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
