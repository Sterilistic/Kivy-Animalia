# -*- coding: utf-8 -*-
__version__ = '0.1'
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.base import runTouchApp

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.


Builder.load_string("""

            
<MenuScreen>:
    GridLayout:
        spacing:10
        padding:10
        cols:2
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        
        Button:
            on_press: root.manager.current = 'settingsA'
            background_normal: str(False)
            Image:
                source: 'icon1.png'
                allow_stretch: True
                y: self.parent.y + self.parent.height - 400
                x: self.parent.x
                size_hint_y: None
                keep_ratio:False 
                size:350,400
           
            
        Button: 
            
            on_press: root.manager.current = 'settingsB' 
            background_normal: str(False)
            Image:
                allow_stretch: True
                source: 'icon2.png'
                y: self.parent.y + self.parent.height - 400
                x: self.parent.x
                size_hint_y: None
                keep_ratio:False 
                size:350,400
        Button:
            on_press: root.manager.current = 'settingsC' 
            background_normal: str(False)
            Image:
                source: 'icon3.png'
                allow_stretch: True
                y: self.parent.y + self.parent.height - 400
                x: self.parent.x
                size_hint_y: None
                keep_ratio:False 
                size:350,400
            
        Button:
            on_press: root.manager.current = 'settingsD'
            background_normal: str(False) 
            Image:
                allow_stretch: True
                source: 'icon4.png'
                y: self.parent.y + self.parent.height - 400
                x: self.parent.x
                size_hint_y: None
                keep_ratio:False 
                size:350,400
        Button:
            on_press: root.manager.current = 'settingsE' 
            background_normal: str(False)
            Image:
                source: 'icon5.png'
                allow_stretch: True
                y: self.parent.y + self.parent.height - 400
                x: self.parent.x
                size_hint_y: None
                keep_ratio:False 
                size:350,400
	   
        Button:
            on_press: root.manager.current = 'settingsF' 
            background_normal: str(False)
            Image:
                source: 'icon6.png'
                allow_stretch: True
                y: self.parent.y + self.parent.height - 400
                x: self.parent.x
                size_hint_y: None
                keep_ratio:False 
                size:350,400
	   
        
<SettingsScreenA>:
    BoxLayout:
        
        
        orientation:'vertical'
        
        Scatter:
            
            size: 100,150
            do_rotation: True
            do_scale: True
            do_translation: True
            auto_bring_to_front: False

            Image:
                source: 'a1.png'
                pos: 320,40
                size_hint: 1, 1
                allow_strech: True
                keep_ratio: True
                size: 100, 150
        ScrollView:
            Label:
                
                size_hint_y: None
                text_size: self.width, None
                size_hint_y: None
                size: self.texture_size
                height: self.texture_size[1]
                
                text: "The koala (Phascolarctos cinereus, or, inaccurately, koala bear[a]) is an arboreal herbivorous marsupial native to Australia. It is the only extant representative of the family Phascolarctidae, and its closest living relatives are the wombats.[3] The koala is found in coastal areas of the mainland's eastern and southern regions, inhabiting Queensland, New South Wales, Victoria, and South Australia. It is easily recognisable by its stout, tailless body and large head with round, fluffy ears and large, spoon-shaped nose. The koala has a body length of 60–85 cm (24–33 in) and weighs 4–15 kg (9–33 lb). Pelage colour ranges from silver grey to chocolate brown. Koalas from the northern populations are typically smaller and lighter in colour than their counterparts further south. These populations possibly are separate subspecies, but this is disputed.Koalas typically inhabit open eucalypt woodlands, and the leaves of these trees make up most of their diet. Because this eucalypt diet has limited nutritional and caloric content, koalas are largely sedentary and sleep up to 20 hours a day. They are asocial animals, and bonding exists only between mothers and dependent offspring. Adult males communicate with loud bellows that intimidate rivals and attract mates. Males mark their presence with secretions from scent glands located on their chests. Being marsupials, koalas give birth to underdeveloped young that crawl into their mothers' pouches, where they stay for the first six to seven months of their lives. These young koalas, known as joeys, are fully weaned around a year old. Koalas have few natural predators and parasites, but are threatened by various pathogens, such as Chlamydiaceae bacteria and the koala retrovirus, as well as by bushfires and droughts.The modern koala is the only extant member of Phascolarctidae, a family that once included several genera and species. During the Oligocene and Miocene, koalas lived in rainforests and had less specialised diets.[14] Some species, such as the Riversleigh rainforest koala (Nimiokoala greystanesi) and some species of Perikoala, were around the same size as the modern koala, while others, such as species of Litokoala, were one-half to two-thirds its size.[15] Like the modern species, prehistoric koalas had well developed ear structures which suggests that long-distance vocalising and sedentism developed early.[14] During the Miocene, the Australian continent began drying out, leading to the decline of rainforests and the spread of open Eucalyptus woodlands. The genus Phascolarctos split from Litokoala in the late Miocene[14][16] and had several adaptations that allowed it to live on a specialised eucalyptus diet: a shifting of the palate towards the front of the skull; larger molars and premolars; smaller pterygoid fossa;[14] and a larger gap between the molar and the incisor teeth.[17]During the Pliocene and Pleistocene, when Australia experienced changes in climate and vegetation, koala species grew larger.[15] P. cinereus may have emerged as a dwarf form of the giant koala (P. stirtoni). The reduction in the size of large mammals has been seen as a common phenomenon worldwide during the late Pleistocene, and several Australian mammals, such as the agile wallaby, are traditionally believed to have resulted from this dwarfing. A 2008 study questions this hypothesis, noting that P. cinereus and P. stirtoni were sympatric during the middle to late Pleistocene, and possibly as early as the Pliocene.[18] The fossil record of the modern koala extends back at least to the middle Pleistocene."
        Button:
            pos:200, 200
            size: 100,150
            on_press:root.manager.current='menu'
            text:'Go Back!!'



<SettingsScreenB>:
    BoxLayout:
        spacing:10
        padding:10
        orientation:'vertical'
        Scatter:
            
            size: 100,150
            do_rotation: True
            do_scale: True
            do_translation: True
            auto_bring_to_front: False

            Image:
                source: 'a2.png'
                pos: 320,40
                size_hint: 1, 1
                allow_strech: True
                keep_ratio: True
                size: 100, 150
        ScrollView:
            Label:
                size_hint_y: None
                text_size: self.width, None
                size_hint_y: None
                size: self.texture_size
                height: self.texture_size[1]
                text: "Elephants are large mammals of the family Elephantidae and the order Proboscidea. Two species are traditionally recognised, the African elephant (Loxodonta africana) and the Asian elephant (Elephas maximus), although some evidence suggests that African bush elephants and African forest elephants are separate species (L. africana and L. cyclotis respectively). Elephants are scattered throughout sub-Saharan Africa, South Asia, and Southeast Asia. Elephantidae is the only surviving family of the order Proboscidea; other, now extinct, members of the order include deinotheres, gomphotheres, mammoths, and mastodons. Male African elephants are the largest extant terrestrial animals and can reach a height of 4 m (13 ft) and weigh 7,000 kg (15,000 lb). Elephants are herbivorous and can be found in different habitats including savannahs, forests, deserts and marshes. They prefer to stay near water. They are considered to be keystone species due to their impact on their environments. Other animals tend to keep their distance; predators such as lions, tigers, hyenas and wild dogs usually target only the young elephants. Females  tend to live in family groups, which can consist of one female with her calves or several related females with offspring. The groups are led by an individual known as the matriarch, often the oldest cow. Elephants have a fission-fusion society in which multiple family groups come together to socialise. Males  leave their family groups when they reach puberty, and may live alone or with other males. Adult bulls mostly interact with family groups when looking for a mate and enter a state of increased testosterone and aggression known as musth, which helps them gain dominance and reproductive success.Elephants belong to the family Elephantidae, the sole remaining family within the order Proboscidea. Their closest extant relatives are the sirenians (dugongs and manatees) and the hyraxes, with which they share the clade Paenungulata within the superorder Afrotheria.[11] Elephants and sirenians are further grouped in the clade Tethytheria.[12] Traditionally, two species of elephants are recognised; the African elephant (Loxodonta africana) of sub-Saharan Africa, and the Asian elephant (Elephas maximus) of South and Southeast Asia. African elephants have larger ears, a concave back, more wrinkled skin, a sloping abdomen and two finger-like extensions at the tip of the trunk. Asian elephants have smaller ears, a convex or level back, smoother skin, a horizontal abdomen that occasionally sags in the middle and one extension at the tip of the trunk. The looped ridges on the molars are narrower in the Asian elephant while those of the African are more diamond-shaped. The Asian elephant also has dorsal bumps on its head and some patches of depigmentation on its skin.[13] In general, African elephants are larger than their Asian cousins. Swedish zoologist Carl Linnaeus first described the genus Elephas and an elephant from Sri Lanka (then known as Ceylon) under the binomial Elephas maximus in 1758. In 1798, Georges Cuvier classified the Indian elephant under the binomial Elephas indicus. Dutch zoologist Coenraad Jacob Temminck described the Sumatran elephant in 1847 under the binomial Elephas sumatranus. English zoologist Frederick Nutter Chasen classified all three as subspecies of the Asian elephant in 1940.[14] Asian elephants vary geographically in their colour and amount of depigmentation. The Sri Lankan elephant (Elephas maximus maximus) inhabits Sri Lanka, the Indian elephant (E. m. indicus) is native to mainland Asia (on the Indian subcontinent and Indochina), and the Sumatran elephant (E. m. sumatranus) is found in Sumatra.[13] One disputed subspecies, the Borneo elephant, lives in northern Borneo and is smaller than all the other subspecies. It has larger ears, a longer tail, and straighter tusks than the typical elephant. Sri Lankan zoologist Paules Edward Pieris Deraniyagala described it in 1950 under the trinomial Elephas maximus borneensis, taking as his type an illustration in National Geographic.[15] It was subsequently subsumed under either E. m. indicus or E. m. sumatranus. Results of a 2003 genetic analysis indicate its ancestors separated from the mainland population about 300,000 years ago.[16] A 2008 study found that Borneo elephants are not indigenous to the island but were brought there before 1521 by the Sultan of Sulu from Java, where elephants are now extinct.[15] "    
        Button:
            valign:'middle'
            size:250, 250	
            on_press:root.manager.current='menu'
            text:'Go Back!!'

<SettingsScreenC>:
    BoxLayout:
        spacing:10
        padding:10
        orientation:'vertical'
        Scatter:
            
            size: 100,150
            do_rotation: True
            do_scale: True
            do_translation: True
            auto_bring_to_front: False

            Image:
                source: 'a3.png'
                pos: 320,40
                size_hint: 1, 1
                allow_strech: True
                keep_ratio: True
                size: 100, 150
        ScrollView:
            Label:
                size_hint_y: None
                text_size: self.width, None
                size_hint_y: None
                size: self.texture_size
                height: self.texture_size[1]
                text: " The domestic dog (Canis lupus familiaris or Canis familiaris) is a domesticated canid which has been selectively bred for millennia for various behaviors, sensory capabilities, and physical attributes.Although initially thought to have originated as a manmade variant of an extant canid species (variously supposed as being the dhole,[3] golden jackal,[4] or gray wolf[5]), extensive genetic studies undertaken during the 2010s indicate that dogs diverged from other wolf-like canids in Eurasia 40,000 years ago.[6] Being the oldest domesticated animals, their long association with people has allowed dogs to be uniquely attuned to human behavior,[7] as well as thrive on a starch-rich diet which would be inadequate for other canid species.Dogs perform many roles for people, such as hunting, herding, pulling loads, protection, assisting police and military, companionship, and, more recently, aiding handicapped individuals. This impact on human society has given them the nickname 'man's best friend' in the Western world. In some cultures, however, dogs are a source of meat.In domestic dogs, sexual maturity begins to happen around age six to twelve months for both males and females,[2][50] although this can be delayed until up to two years old for some large breeds. This is the time at which female dogs will have their first estrous cycle. They will experience subsequent estrous cycles biannually, during which the body prepares for pregnancy. At the peak of the cycle, females will come into estrus, being mentally and physically receptive to copulation.[2] Because the ova survive and are capable of being fertilized for a week after ovulation, it is possible for a female to mate with more than one male.[2]2–5 days post conception fertilization occurs, 14–16 days embryo attaches to uterus 22–23 days heart beat is detectable.[51][52]Dogs bear their litters roughly 58 to 68 days after fertilization,[2][53] with an average of 63 days, although the length of gestation can vary. An average litter consists of about six puppies,[54] though this number may vary widely based on the breed of dog. In general, toy dogs produce from one to four puppies in each litter, while much larger breeds may average as many as twelve.Some dog breeds have acquired traits through selective breeding that interfere with reproduction. Male French Bulldogs, for instance, are incapable of mounting the female. For many dogs of this breed, the female must be artificially inseminated in order to reproduce.[55]"    
        Button:
            valign:'middle'
            size:250, 250	
            on_press:root.manager.current='menu'
            text:'Go Back!!'
<SettingsScreenD>:
    BoxLayout:
        spacing:10
        padding:10
        orientation:'vertical'
        Scatter:
            
            size: 100,150
            do_rotation: True
            do_scale: True
            do_translation: True
            auto_bring_to_front: False

            Image:
                source: 'a4.png'
                pos: 320,40
                size_hint: 1, 1
                allow_strech: True
                keep_ratio: True
                size: 100, 150
        ScrollView:
            Label:
                size_hint_y: None
                text_size: self.width, None
                size_hint_y: None
                size: self.texture_size
                height: self.texture_size[1]
                text: "Zebras (/ˈzɛbrə/ ZEB-rə or /ˈziːbrə/ ZEE-brə)[1] are several species of African equids (horse family) united by their distinctive black and white striped coats. Their stripes come in different patterns, unique to each individual. They are generally social animals that live in small harems to large herds. Unlike their closest relatives, horses and donkeys, zebras have never been truly domesticated.There are three species of zebras: the plains zebra, the Grévy's zebra and the mountain zebra. The plains zebra and the mountain zebra belong to the subgenus Hippotigris, but Grévy's zebra is the sole species of subgenus Dolichohippus. The latter resembles an ass, to which it is closely related, while the former two are more horse-like. All three belong to the genus Equus, along with other living equids.The unique stripes of zebras make them one of the animals most familiar to people. They occur in a variety of habitats, such as grasslands, savannas, woodlands, thorny scrublands, mountains, and coastal hills. However, various anthropogenic factors have had a severe impact on zebra populations, in particular hunting for skins and habitat destruction. Grévy's zebra and the mountain zebra are endangered. While plains zebras are much more plentiful, one subspecies, the quagga, became extinct in the late 19th century – though there is currently a plan, called the Quagga Project, that aims to breed zebras that are phenotypically similar to the quagga in a process called breeding back.The plains zebra (Equus quagga, formerly Equus burchelli) is the most common, and has or had about six subspecies distributed across much of southern and eastern Africa. It, or particular subspecies of it, have also been known as the common zebra, the dauw, Burchell's zebra (actually the subspecies Equus quagga burchellii), Chapman's zebra, Wahlberg's zebra, Selous' zebra, Grant's zebra, Boehm's zebra and the quagga (another extinct subspecies, Equus quagga quagga).The mountain zebra (Equus zebra) of southwest Africa tends to have a sleek coat with a white belly and narrower stripes than the plains Zebra. It has two subspecies and is classified as vulnerable.Grévy's zebra (Equus grevyi) is the largest type, with a long, narrow head, making it appear rather mule-like. It is an inhabitant of the semi-arid grasslands of Ethiopia and northern Kenya. Grévy's zebra is the rarest species, and is classified as endangered.Although zebra species may have overlapping ranges, they do not interbreed. In captivity, plains zebras have been crossed with mountain zebras. The hybrid foals lacked a dewlap and resembled the plains zebra apart from their larger ears and their hindquarters pattern. Attempts to breed a Grévy's zebra stallion to mountain zebra mares resulted in a high rate of miscarriage. In captivity, crosses between zebras and other (non-zebra) equines have produced several distinct hybrids, including the zebroid, zeedonk, zony, and zorse. In certain regions of Kenya, plains zebras and Grévy's Zebra coexist, and fertile hybrids occur. "    
        Button:
            valign:'middle'
            size:250, 250	
            on_press:root.manager.current='menu'
            text:'Go Back!!'
<SettingsScreenE>:
    BoxLayout:
        spacing:10
        padding:10
        orientation:'vertical'
        Scatter:
            
            size: 100,150
            do_rotation: True
            do_scale: True
            do_translation: True
            auto_bring_to_front: False

            Image:
                source: 'a5.png'
                pos: 320,40
                size_hint: 1, 1
                allow_strech: True
                keep_ratio: True
                size: 100, 150
        ScrollView:
            Label:
                size_hint_y: None
                text_size: self.width, None
                size_hint_y: None
                size: self.texture_size
                height: self.texture_size[1]
                text: " Squirrels are generally small animals, ranging in size from the African pygmy squirrel at 7–10 cm (2.8–3.9 in) in length and just 10 g (0.35 oz) in weight, to the Alpine marmot, which is 53–73 cm (21–29 in) long and weighs from 5 to 8 kg (11 to 18 lb). Squirrels typically have slender bodies with bushy tails and large eyes. In general, their fur is soft and silky, although much thicker in some species than others. The color of squirrels is highly variable between—and often even within—species.[5]In general, the hind limbs are longer than the fore limbs, and they have four or five toes on each paw. Their paws include an often poorly developed thumb, and have soft pads on the undersides.[6] Unlike most mammals, Tree squirrels can descend a tree head-first. They do so by rotating their ankles 180 degrees so the hind paws are backward-pointing and can grip the tree bark.[7]Squirrels live in almost every habitat from tropical rainforest to semiarid desert, avoiding only the high polar regions and the driest of deserts. They are predominantly herbivorous, subsisting on seeds and nuts, but many will eat insects and even small vertebrates.[8]Squirrels cannot digest cellulose, so they must rely on foods rich in protein, carbohydrates, and fats. In temperate regions, early spring is the hardest time of year for squirrels, because buried nuts begin to sprout and are no longer available for the squirrel to eat, and new food sources have not become available yet. During these times, squirrels rely heavily on the buds of trees. Squirrels' diets consist primarily of a wide variety of plants, including nuts, seeds, conifer cones, fruits, fungi, and green vegetation. However, some squirrels also consume meat, especially when faced with hunger.[8] Squirrels have been known to eat insects, eggs, small birds, young snakes, and smaller rodents. Indeed, some tropical species have shifted almost entirely to a diet of insects.[13]Predatory behavior has been noted by various species of ground squirrels, in particular the thirteen-lined ground squirrel.[14] For example, Bailey, a scientist in the 1920s, observed a thirteen-lined ground squirrel preying upon a young chicken.[15] Wistrand reported seeing this same species eating a freshly killed snake.[16] Whitaker examined the stomachs of 139 thirteen-lined ground squirrels and found bird flesh in four of the specimens and the remains of a short-tailed shrew in one;[17] Bradley, examining white-tailed antelope squirrels' stomachs, found at least 10% of his 609 specimens' stomachs contained some type of vertebrate, mostly lizards and rodents.[18] Morgart observed a white-tailed antelope squirrel capturing and eating a silky pocket mouse."    
        Button:
            valign:'middle'
            size:250, 250	
            on_press:root.manager.current='menu'
            text:'Go Back!!'
<SettingsScreenF>:
    BoxLayout:
        spacing:10
        padding:10
        orientation:'vertical'
        Scatter:
            
            size: 100,150
            do_rotation: True
            do_scale: True
            do_translation: True
            auto_bring_to_front: False

            Image:
                source: 'a6.png'
                pos: 320,40
                size_hint: 1, 1
                allow_strech: True
                keep_ratio: True
                size: 100, 150
        ScrollView:
            Label:
                size_hint_y: None
                text_size: self.width, None
                size_hint_y: None
                size: self.texture_size
                height: self.texture_size[1]
                text: "Rabbits are hindgut digesters. This means that most of their digestion takes place in their large intestine and cecum. In rabbits, the cecum is about 10 times bigger than the stomach and it along with the large intestine makes up roughly 40% of the rabbit's digestive tract.[7] The unique musculature of the cecum allows the intestinal tract of the rabbit to separate fibrous material from more digestible material; the fibrous material is passed as feces, while the more nutritious material is encased in a mucous lining as a cecotrope. Cecotropes, sometimes called 'night feces', are high in minerals, vitamins and proteins that are necessary to the rabbit's health. Rabbits eat these to meet their nutritional requirements; the mucous coating allows the nutrients to pass through the acidic stomach for digestion in the intestines. This process allows rabbits to extract the necessary nutrients from their food.[8]Rabbits are prey animals and are therefore constantly aware of their surroundings. For instances, in Mediterranean Europe, rabbits are the main prey of red foxes, badgers, and Iberian lynxes.[9] If confronted by a potential threat, a rabbit may freeze and observe then warn others in the warren with powerful thumps on the ground. Rabbits have a remarkably wide field of vision, and a good deal of it is devoted to overhead scanning.[10] They survive predation by burrowing, hopping away in a zig-zag motion, and, if captured, delivering powerful kicks with their hind legs. Their strong teeth allow them to eat and to bite in order to escape a struggle.[11] The expected wild rabbit lifespan is about 3 years.Rabbits are herbivores that feed by grazing on grass, forbs, and leafy weeds. In consequence, their diet contains large amounts of cellulose, which is hard to digest. Rabbits solve this problem via a form of hindgut fermentation. They pass two distinct types of feces: hard droppings and soft black viscous pellets, the latter of which are known as caecotrophs and are immediately eaten (a behaviour known as coprophagy). Rabbits reingest their own droppings (rather than chewing the cud as do cows and many other herbivores) to digest their food further and extract sufficient nutrients.[14]Rabbits graze heavily and rapidly for roughly the first half hour of a grazing period (usually in the late afternoon), followed by about half an hour of more selective feeding. In this time, the rabbit will also excrete many hard fecal pellets, being waste pellets that will not be reingested. If the environment is relatively non-threatening, the rabbit will remain outdoors for many hours, grazing at intervals. While out of the burrow, the rabbit will occasionally reingest its soft, partially digested pellets; this is rarely observed, since the pellets are reingested as they are produced. Reingestion is most common within the burrow between 8 o'clock in the morning and 5 o'clock in the evening, being carried out intermittently within that period."    
        Button:
            valign:'middle'
            size:250, 250	
            on_press:root.manager.current='menu'
            text:'Go Back!!'


            

""")



# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreenA(Screen):
    pass


class SettingsScreenB(Screen):
    pass
class SettingsScreenC(Screen):
    pass
class SettingsScreenD(Screen):
    pass
class SettingsScreenE(Screen):
    pass
class SettingsScreenF(Screen):
    pass
# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreenA(name='settingsA'))
sm.add_widget(SettingsScreenB(name='settingsB'))
sm.add_widget(SettingsScreenC(name='settingsC'))
sm.add_widget(SettingsScreenD(name='settingsD'))
sm.add_widget(SettingsScreenE(name='settingsE'))
sm.add_widget(SettingsScreenF(name='settingsF'))

class TestApp(App):
    def build(self):
        return sm
        

if __name__ == '__main__':
    TestApp().run()
