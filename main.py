import json
import time
import colorama
import requests

from colorama import Fore

class Main:
    def __init__(self) -> None:
        colorama.init(autoreset=True)

    def LocChunksLoader(self):
        with open('datas/PakChunks.json', 'r') as aes:
            aes = json.load(aes)

        for i in aes['allPakFiles']:
            if i.startswith('FortniteGame/Content/Paks/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Loaded: " + Fore.GREEN + path)


    def NewFeaturedIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Outfit/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Outfit/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)

    def NewBackpacksIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/Icons/Backpacks/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/Icons/Backpacks/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content) 

    def NewEmotesIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Emotes/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Emotes/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)

    def NewWrapsIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/Icons/Wraps/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/Icons/Wraps/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content) 

    def NewPickaxeIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Pickaxe/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Pickaxe/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content) 

    def NewWeaponsIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Plugins/GameFeatures/CorruptionGameplay/Content/Gameplay/Icons/'):
                if i.endswith('-L.uasset'):
                    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.RED + "Skipped " + Fore.CYAN + path)
                else:
                    path = i
                    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                    image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                    pathname = (path.split('FortniteGame/Plugins/GameFeatures/CorruptionGameplay/Content/Gameplay/Icons/')[-1])
                    open(f'images/{pathname}.png', 'wb+').write(image.content) 

    def NewMusicsIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/2dAssets/Music/Season18/PreviewImages/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split('FortniteGame/Content/2dAssets/Music/Season18/PreviewImages/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)

    def NewVariantsIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/Athena/Items/CosmeticVariantTokens/'):
                path = i
                path1 = i.replace('.uasset', '')
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/assetProperties?path={path1}')
                x = image.json()['export_properties'][0]
                assetpath = x['LargePreviewImage']['assetPath']
                url = f'https://benbot.app/api/v1/exportAsset?path={assetpath}'
                r = requests.get(url)
                pathname = (path.split('FortniteGame/Content/Athena/Items/CosmeticVariantTokens/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(r.content)

        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/Icons/Heroes/Athena/Soldier/'):
                if i.endswith('-L.uasset'):
                    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.RED + "Skipped " + Fore.CYAN + path)
                else:
                    path = i
                    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                    image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                    pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/Icons/Heroes/Athena/Soldier/')[-1])
                    open(f'images/{pathname}.png', 'wb+').write(image.content)

    def NewCosmeticsIcons(self):
        with open('datas/NewCosmetics.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons['data']['items']:
            id = i['id']
            image = i['images']['icon']
            r = requests.get(image)
            open(f'images/{id}.png', 'wb+').write(r.content)
            print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + i['path'])

    def NewCreativeIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/Athena/Items/Consumables/PlaysetGrenade/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split('FortniteGame/Content/Athena/Items/Consumables/PlaysetGrenade/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)   


    # sound extractor made by Leaks Station  

    def NewSounds(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons :
            if i.startswith('FortniteGame/Content/Sounds/'):
                path = i
                sound = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                for x in path :
                    if x == "_" :
                        path = path.replace('_', '-')
                    if x == "/":
                        path = path.replace('/', '-')
                    path = path.replace("FortniteGame-Content-Sounds-","")
                open(f'sounds/{path}.ogg', 'wb+').write(sound.content) 
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Saving: " + Fore.GREEN + path)
                
            

    def main(self):
        print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Geneating data..")
        newcosmetics = requests.get('https://fortnite-api.com/v2/cosmetics/br/new').json()
        aes = requests.get('https://benbot.app/api/v1/status').json()
        newassets = requests.get('https://benbot.app/api/v1/files/added').json()
        with open('datas/NewCosmetics.json', 'w') as file:
            json.dump(newcosmetics, file, indent=2)
        with open('datas/PakChunks.json', 'w') as file:
            json.dump(aes, file, indent=2)    
        with open('datas/NewAssets.json', 'w') as file:
            json.dump(newassets, file, indent=2)  
        start = time.time()
        print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing..")
        self.LocChunksLoader()
        self.NewBackpacksIcons()
        self.NewCreativeIcons()
        self.NewEmotesIcons()
        self.NewPickaxeIcons()
        self.NewVariantsIcons()
        self.NewMusicsIcons()
        self.NewCosmeticsIcons()
        #self.NewWrapsIcons()
        self.NewWeaponsIcons()
        self.NewSounds()
        end = time.time()
        print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)}")


if __name__ == "__main__":
    try:
        Main().main()
    except KeyboardInterrupt:
        exit(5)