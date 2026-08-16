{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d04b7c9-f8c2-40ca-ac70-ba2eb94f0572",
   "metadata": {},
   "outputs": [],
   "source": [
    "a=int(input(\"enter the first number:\"))\n",
    "b=int(input(\"enter the second number:\"))\n",
    "c=int(input(\"enter the third number:\"))\n",
    "if a==b==c:\n",
    "    print(\"all numbers are equal\")\n",
    "elif a==b and a>c:\n",
    "    print(\"a and b are equal and they are the largest\")\n",
    "elif a==c and a>b:\n",
    "    print(\"a and c are equal and they are the largest\")\n",
    "elif b==c and b>a:\n",
    "    print(\"b and c are equal and they are the largest\")\n",
    "elif a>b and a>c:\n",
    "    print(\"a is the largest\")\n",
    "elif b>a and b>c:\n",
    "    print(\"b is the largest\")\n",
    "else:\n",
    "    print(\"c is the largest\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e755a0a-bc54-4956-a114-2724f3f1de6e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
