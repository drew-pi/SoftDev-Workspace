# Andrew Piatetsky (Wolfgang)
# SoftDev
# K14 - css and flask TOGETHER
# 2022-10-19
# time spent: 30 mins

from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

ipsum = [
    "Pommy ipsum cottage pie therewith gobsmacked a right toff, that's ace old girl hedgehog brainbox clock round the earhole the lakes, full English breakast posh nosh air one's dirty linen utter shambles. Jellied eels what a mug bog roll oo ecky thump bull dog full English breakast, hard cheese old boy Prince Charles completely crackers. Queer as a clockwork orange rumpy pumpy lad Doctor Who cotton on The Doctor, gob hard cheese old boy grub's up jolly. Golly gosh damn got his end away on't goggle box chaps, rather stiff upper lip the lakes scrumpy willy, gobsmacked pork dripping lass.",
    "Bit of alright tad copper cobbles dignified lost the plot sod's law, fancied a flutter it's the bees knees chuffed got a lot of brass marmite. God save the queen on his tod superb bread and butter pudding meat and two veg blummin', ridicule gobsmacked scally made a pig's ear of it, Queen Elizabeth tip-top pants bow ties are cool. Quid Sonic Screwdriver the lakes on the beat off t'shop sweet fanny adams quid, old chap scrumpy gallivanting around absolute twoddle a bit miffed Kate and Will a cracking, ever so lovely codswallop lad pants and we all like figgy pudding.",
    "Big light wibbly-wobbly timey-wimey stuff curry sauce some mothers do 'ave 'em stew and dumps ever so lovely lass pulled out the eating irons, challenge you to a duel Sherlock old chap argy-bargy pants flip flops. Dalek Elementary my dear Watson working class what a mug crisps superb one off, got his end away chips macca cotton on a total jessie a tad what a mug, chav fried toast alright geezer marmite knackered. Jammy git scouser brilliant fancied a flutter a bottle of plonk a tad, chin up Moriarty smeg head cobbles, bogroll cottage pie codswallop yorkshire pudding."
]


@app.route("/")
def root():
    return index()


@app.route("/index", methods=["GET"]) # default route
def index():
    # all we are doing is filling in the variable
    return render_template('index.html',
                            p1=ipsum[0],
                            p2=ipsum[1],
                            p3=ipsum[2])


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
