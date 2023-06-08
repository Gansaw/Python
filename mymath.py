{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "eae6e590",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add(x, y):\n",
    "    return x + y\n",
    "\n",
    "def subtract(x, y):\n",
    "    return x - y\n",
    "\n",
    "def multiply(x, y):\n",
    "    return x * y\n",
    "\n",
    "def divide(x, y):\n",
    "    if y == 0:\n",
    "        return \"0으로 나눌 수 없습니다.\"\n",
    "    else:\n",
    "        return x / y\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    x = 4\n",
    "    y = 3\n",
    "\n",
    "    print(add(x, y))\n",
    "    print(subtract(x, y))\n",
    "    print(multiply(x, y))\n",
    "    print(divide(x, y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0ee51465",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\user\\\\Python_jupyter\\\\Python\\\\Class2'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "os.getcwd()"
   ]
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
