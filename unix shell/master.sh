###############help
##man command
##man -f command shows chapters of help man pages
##man number command direct job to help pages
##man -a command all pages
##info command like webpage links
##command--help

###file descriptors are standard-in(0) stantard-out(1) stantard-err(3). Other file descriptors starts with 3
##stores standard input in input file
sh sample.sh 0>in.txt
##stores standard out in output file
sh sample.sh 1>out.txt
##stores standard err in err file
sh sample.sh 2>err.txt
##stores all  in a file
sh sample.sh >allout.txt 2>&1
##pipe helps to run more than 1 command in the same time,
##moreover it helps to save diskspace as there is no need to save outputs in temporary files 
##command1|command2|command3
a=`expr 1+1`| echo $a
##locate helps to file recently created files
##locate uses updatedb. which runs daily
locate tutorial | grep q1>test.txt
##refreshes db
sudo updatedb
## ?  	Matches any single character
locate ?.txt | grep poc
## * 	Matches any string of characters
locate *.txt | grep poc
## [set] 	Matches any character in the set of characters, for example [adf] will match any occurrence of "a", "d", or "f"
## [!set] 	Matches any character not in the set of characters
locate [t].txt | grep poc
##find helps to find a file. which is mostly used by administators
find test.txt
##Another good use of find is being able to run commands on the files that match your search criteria. The -exec option is used for this ##purpose.
##To find and remove all files that end with .swp:
##$ find -name "*.swp" -exec rm {} ’;’
find sample.sh -exec sh {} \;
## -ok option will ask for permission
##find sample.sh -ok sh {} \;
###Finding based on time:
##$ find / -ctime 3
##Here, -ctime is when the inode meta-data (i.e., file ownership, permissions, etc) last changed; it is often, but not necessarily when the ##file was first created. You can also search for accessed/last read (-atime) or modified/last written (-mtime) times. The number is the number ##of days and can be expressed as either a number (n) that means exactly that value, +n which means greater than that number, or -n which means ##less than that number. There are similar options for times in minutes (as in -cmin, -amin, and -mmin).
###Finding based on sizes:
##$ find / -size 0
##Note the size here is in 512-byte blocks, by default; you can also specify bytes (c), kilobytes (k), megabytes (M), gigabytes (G), etc. As ##with the time numbers above, file sizes can also be exact numbers (n), +n or -n. For details consult the man page for find.
##For example, to find files greater than 10 MB in size and running a command on those files:
##$ find / -size +10M -exec command {} ’;’
find /home -size +10M
## -name option for filename
find -name test.txt
## -type option for filetype
find -name test.txt -type f

##############Working with files

###cat 	Used for viewing files that are not very long; it does not provide any scroll-back.
###tac 	Used to look at a file backwards, starting with the last line.
###less 	Used to view larger files because it is a paging program; it pauses at each screenful of text, provides scroll-back #capabilities, and lets you search and navigate within the file. Note: Use / to search for a pattern in the forward direction and ? for a #pattern in the backward direction.
###tail 	Used to print the last 10 lines of a file by default. You can change the number of lines by doing -n 15 or just -15 if you #wanted to look at the last 15 lines instead of the default.
###head 	The opposite of tail; by default it prints the first 10 lines of a file.


###############Removing files
##mv 	Rename a file 
##rm 	Remove a file 
##rm –f 	Forcefully remove a file
##	rm –i 	Interactively remove a file

################directories 
##mv 	Rename a directory
##rmdir 	Remove an empty directory
##rm -rf 	Forcefully remove a directory recursively (delete directory with entries)

##create empty file with timestampe 
##touch -t YYMMDDHHMM file name
touch -t 2012310000 yearend

#######################installation
#Both package management systems provide two tool levels: a low-level tool (such as dpkg or rpm), takes care of the details of unpacking #individual packages, running scripts, getting the software installed correctly, while a high-level tool (such as apt-get, yum, or zypper) #works with groups of packages, downloads packages from the vendor, and figures out dependencies.
##install highlevel
#sudo apt-get install tree
##search a package
#sudo apt-cache search tree
##check installation
#sudo apt-cache policy tree
##remove installation
#sudo apt-get remove tree
##upgrade packages 
#sudo apt-get upgrade

###################filesystem
##df -Th shows amount space avaiable
df -Th 


#################processes
##ps 	Produces a list of processes along with status information for the system.
##ls 	Produces a listing of the contents of a directory.
##cp 	Used to copy files.


####all devices in linux are like files. connected devices will seen in /dev/
##/var stores the files which varies /var/lib /var/log

###The /boot Directory

##The /boot directory contains the few essential files needed to boot the system. For every alternative kernel installed on the system there ##are four files:

##vmlinuz: the compressed Linux kernel, required for booting
##initramfs: the initial ram filesystem, required for booting, sometimes called initrd, not initramfs
##config: the kernel configuration file, only used for debugging and bookkeeping
##System.map: kernel symbol table, only used for debugging


###comparing files 
##diff -c helps to find differences 	
##diff -c file1 file2
##diff3 compare 3 files
##file filename displays type of file 


##rsync is most efficient way of copying files than cp. resync checks file it is already present,copies only changedpart 
##and also to other machines
#rsync sourcefile/sourcefolder destinationfile/destination folder


##############compression
##gzip 	The most frequently used Linux compression utility
##bzip2 	Produces files significantly smaller than those produced by gzip
##xz 	The most space efficient compression utility used in Linux
##zip 	Is often required to examine and decompress archives from other operating systems

##gzip * 	Compresses all files in the current directory; each file is compressed and renamed with a .gz extension.
##gzip -r projectX 	Compresses all files in the projectX directory along with all files in all of the directories under projectX.
##gunzip foo 	De-compresses foo found in the file foo.gz. Under the hood, gunzip command is actually the same as gzip –d.

##bzip2 * 	Compress all of the files in the current directory and replaces each file with a file renamed with a .bz2 extension.
##bunzip2 *.bz2 Decompress all of the files with an extension of .bz2 in the current directory. Under the hood, bunzip2 is the same as calling ##bzip2 -d


##xz * 	Compress all of the files in the current directory and replace each file with one with a .xz extension.
##xz foo 	Compress the file foo into foo.xz using the default compression level (-6), and remove foo if compression succeeds.
##xz -dk bar.xz 	Decompress bar.xz into  bar and don't remove bar.xz even if decompression is successful.
##xz -dcf a.txt b.txt.xz > abcd.txt 	Decompress a mix of compressed and uncompressed files to standard output, using a single command.
##xz -d *.xz 	Decompress the files compressed using xz.
