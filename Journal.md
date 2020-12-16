# Lab 4 Journal

## WEEK 1

###### 12/14/2020 - 5:53pm - 7:36pm (1h 43min)

I finished problem 1 (DNA), problem 2 (RNA), problem 3 (REVC), and problem 4 (IPRB). I created a stuff.py for things that I might use again so I can just import it. For now I just have a read file function. I found the first three problems simple, but I struggled with the inheritance probability problem. In the end, I drew a diagram to help me understand how the probabilities worked, and after that it was fine. Halfway through I was debating whether or not to brute force it, but I decided not to :)

###### 12/16/2020 - 1:24pm - 2:36pm (1h 12min)

I started work on problem 5 (FIB) on monday, so I wanted to finish it. I was having a lot of trouble, mostly because I read the question wrong, and thought it was talking about individual rabbits instead of pairs. I then did problem 6 (GC), which I found easier than FIB. I renamed stuff.py to resources.py, and added  the `read_fasta(file_path)` function to it (which I yoinked from lab 2). I learned how to use the `max()`function to find which sequence had the highest GC content.

###### 12/16/2020 - 5:30pm - 

Problem 7 (HAMM) was relatively simple, I just used compared each index of the sequences. For problem 8 (PROT) I repurposed the codon dicts from lab 2, painstakingly changing each T to a U for RNA, which I added to the resources module. Problem 9 was similar to what we did in `findORF()` where I used .find to find the index of all the motifs. *note to self, lists in rosalind are strings with spaces. I think doing these problems before lab 2 would really help because it sort of builds up to it. Problem 10 (CONS) looked complicated at first because of the matrices, but it turned out to be not too difficult. One roadblock I had was submitting it to rosalind, and I ended up creating a `write_file()` function in resources and submitting a text file. I think it messed up because of how long each line is. For problem 11 (FIBD), I originally created a rabbit class with an age property. This worked for the sample dataset, but when I downloaded the actual dataset, I ran into a problem where it would take my computer way too much time after I got past 32 months. I ended up using a dictionary to keep track of ages, which is much much faster than millions of objects.
