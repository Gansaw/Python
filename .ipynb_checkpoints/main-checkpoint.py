{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9b00eef3",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[5], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmymath\u001b[39;00m\n\u001b[0;32m      3\u001b[0m x \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m4\u001b[39m\n\u001b[0;32m      4\u001b[0m y \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m3\u001b[39m\n",
      "File \u001b[1;32m~\\Python_jupyter\\Python\\mymath.py:5\u001b[0m\n\u001b[0;32m      1\u001b[0m {\n\u001b[0;32m      2\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcells\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m      3\u001b[0m   {\n\u001b[0;32m      4\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m----> 5\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[43mnull\u001b[49m,\n\u001b[0;32m      6\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124meae6e590\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      7\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m      8\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m      9\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     10\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef add(x,y):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     11\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    return x + y\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     12\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef subtract(x,y):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     13\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    return x - y\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     14\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef multiply(x,y):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     15\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    return x * y\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     16\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef divide(x,y):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     17\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    if y == 0:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     18\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        return \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m0으로 나눌 수 없습니다.\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     19\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    else:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     20\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        return x / y\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     21\u001b[0m    ]\n\u001b[0;32m     22\u001b[0m   }\n\u001b[0;32m     23\u001b[0m  ],\n\u001b[0;32m     24\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     25\u001b[0m   \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mkernelspec\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     26\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_name\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPython 3 (ipykernel)\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     27\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlanguage\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     28\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     29\u001b[0m   },\n\u001b[0;32m     30\u001b[0m   \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlanguage_info\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     31\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcodemirror_mode\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     32\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mipython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     33\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mversion\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m3\u001b[39m\n\u001b[0;32m     34\u001b[0m    },\n\u001b[0;32m     35\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfile_extension\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m.py\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     36\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmimetype\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/x-python\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     37\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     38\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbconvert_exporter\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     39\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpygments_lexer\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mipython3\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     40\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mversion\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3.10.9\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     41\u001b[0m   }\n\u001b[0;32m     42\u001b[0m  },\n\u001b[0;32m     43\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbformat\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m4\u001b[39m,\n\u001b[0;32m     44\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbformat_minor\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m5\u001b[39m\n\u001b[0;32m     45\u001b[0m }\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import mymath\n",
    "\n",
    "x = 4\n",
    "y = 3\n",
    "\n",
    "print(mymath.add(x,y))\n",
    "print(mymath.subtract(x,y))\n",
    "print(mymath.multiply(x,y))\n",
    "print(mymath.divide(x,y))"
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
