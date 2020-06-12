import os 
import shutil
import re

class Files:

    VIDEO_TYPES = { ".mkv" }
    MATCH_REGEX = { 
        "^\[HorribleSubs\] Ace of Diamond Act II": "Ace of Diamond Act II" , "^\[HorribleSubs\] One Piece": "One Piece",
         "^\[HorribleSubs\] Kimetsu no Yaiba ": "Kimetsu no Yaiba", "^\[HorribleSubs\] Megalo Box": "Megalo Box",
         "^\[HorribleSubs\] Dororo": "Dororo",
         "^\[Golumpa\] My Hero Academia S4": "Boku no Hero Academia","\[HorribleSubs\] Boku no Hero Academia":"Boku no Hero Academia sub",
         "Young.Justice.S03":"Young Justice Season 3","Black.Lightning.S03":"Black Lightning",
         "^Supergirl\.S05": "Supergirl", "The.Flash.2014":"The Flash",
         "Arrow": "Arrow", "^\[HorribleSubs\] Vinland Saga":"Vinland Saga",
         "The.Mandalorian": "The Mandalorian", "Rick.and.Morty.":"Rick and Morty",
         "^\[HorribleSubs\] Haikyuu!!": "Haikyuu",
        "The\.Magicians": "The Magicians",
        "Star.Wars.*The.*Clone.*Wars.": "Star Wars The Clone Wars."
    }

    def __init__(self,folder=r"D:\Downloads 2"):
        self.root = folder
        self.all_files = self.getAllFiles()
        self.all_videos = self.getVideos()
        self.directories = self.getDirectories()
        self.organize()
    
    def getDirectories(self):
        return list(filter(lambda x: os.path.isdir(  os.path.join(self.root,x)  ),self.all_files))
    
    def getAllFiles(self):
        return os.listdir(self.root)

    def getExtension(self,fpath):
        return os.path.splitext(fpath)[1]

    def isVideo(self,fpath):
        return self.getExtension(fpath) in self.VIDEO_TYPES
    
    def getVideos(self):
        return list(filter(lambda x: self.isVideo(x) ,self.all_files ))

    def matchRegex(self,reg,files):
        return filter(lambda x: re.search(reg, x) ,files )
    
    def organize(self):
       
        for pattern,title in self.MATCH_REGEX.items():
            dest = os.path.join(self.root,title)

            

            match = self.matchRegex(pattern,self.all_videos)
            match_dir = self.matchRegex(pattern,self.directories)
            # print(list(self.directories))

            if not os.path.isdir(dest) and (len(match) > 0 or len(match_dir) > 0):
                os.mkdir(dest)

            for search in match:
                try:
                    src = os.path.join(self.root,search)
                    shutil.move(src, dest)
                except shutil.Error as e:
                    print("missed a file")
                    print(e.args[0])
                

            for s in match_dir:
                try:
                    src = os.path.join(self.root,s)
                    shutil.move(src, dest)
                except shutil.Error as e:
                    print("missed a folder")
                    print(e.args[0])
                





org = Files(r"D:\Downloads 2")
# print(org.all_files)
# print(org.matchRegex("^\[HorribleSubs\] Ace of Diamond Act II"))
