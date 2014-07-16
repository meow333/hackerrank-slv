import math
def pc(n):
    p=2
    f=0
    while p<(n/2)+1:
        if n%p==0:
            return False
        p=p+1
    return True

a={'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
l=''
for i in a:
    if pc(a[i]) == True:
        l=l+i+' '
print(l)
m=''
for k in range(198):
    if pc(k) == True:
        m=m+chr(k)#+' '
print(m)

print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))
print(ord('0'))
print(ord('9'))

c='ace, aces, acme, acmes, ae, ag, age, ages, am, as, ask, askew, aw, awe, awes, ba, back, backs, bag, bags, bake, bakes, bam, bams, bas, base, bask, be, beak, beaks, beam, beams, beck, becks, beg, begs, bema, bemas, cab, cabs, cage, cages, cake, cakes, cam, came, cames, cams, case, cask, caw, caws, cwm, cwms, em, ems, es, gab, gabs, gae, gaes, gam, gamb, gambe, gambes, gambs, game, games, gams, gas, gawk, gawks, geck, gecks, gem, gems, ka, kab, kabs, kae, kaes, kame, kames, kas, kea, keas, keg, kegs, ma, mabe, mabes, mac, mace, maces, mack, macks, macs, mae, maes, mag, mage, mages, mags, make, makes, mas, mask, maskeg, maw, maws, me, mesa, mew, mews, sab, sabe, sac, sack, sae, sag, sage, sake, same, samek, saw, scab, scag, scam, sea, seam, sec, seg, sew, ska, skag, skeg, skew, smack, smew, swab, swag, swage, swam, wab, wabs, wack, wacke, wackes, wacks, wae, waes, wag, wage, wages, wags, wake, wakes, wame, wames, was, we, weak, web, webs, weka, wekas'
d=c.split(', ')

e='ace, aces, acme, acmes, ae, aegis, ag, age, ageism, ages, aggie, aggies, agio, agios, agism, ago, agog, ai, aim, aims, ais, am, ami, amice, amices, amie, amies, amigo, amigos, amis, amok, amoks, as, asci, ask, askoi, ay, aye, ayes, ays, cage, cages, cagey, cagy, cake, cakes, cakey, caky, cam, came, cameo, cameos, cames, camise, cams, case, cask, casky, cay, cays, ciao, cis, cog, cogs, coke, cokes, coma, comae, comake, comakes, comas, come, comes, cos, cosey, cosie, cosy, coy, coys, cyma, cymae, cymas, cyme, cymes, cymose, easy, egg, eggs, eggy, egis, ego, egoism, egos, em, emic, ems, es, eyas, gae, gaes, gag, gage, gages, gags, gam, game, games, gamey, gamic, gams, gamy, gas, gay, gays, geck, gecko, geckos, gecks, gem, gems, gey, gie, gies, gig, giga, gigas, gigs, gismo, go, goa, goas, goes, gym, gyms, ice, ices, ick, icky, icy, image, images, imago, imagoes, imagos, is, isagoge, ism, isogamy, ka, kae, kaes, kame, kames, kami, kas, kay, kayo, kayoes, kayos, kays, kea, keas, keg, kegs, key, keys, koa, koas, kos, ma, mac, mace, maces, mack, macks, macs, mae, maes, mag, mage, mages, magi, magic, magics, mags, make, makes, mako, makos, mas, mask, maskeg, may, mayo, mayos, mays, me, mesa, mesic, mi, mica, micas, mice, mickey, mickeys, mig, migg, miggs, migs, mike, mikes, mis, mise, miso, misyoke, mo, moa, moas, mock, mocks, mog, mogs, moke, mokes, mos, mosaic, mosey, mosk, my, oak, oaks, oca, ocas, oe, oes, ogam, ogams, oka, okas, okay, okays, oke, okes, om, omega, omegas, oms, os, ose, osmic, oy, oyes, sac, sack, sae, sag, sage, saggy, sago, sagy, saice, sake, saki, same, samek, say, scag, scam, sea, seam, seamy, sec, seg, sego, sei, semi, si, sic, sice, sick, sicko, sigma, sike, sim, sima, ska, skag, skeg, ski, skiey, skim, sky, smack, smock, smog, smoggy, smoke, smokey, smoky, so, soak, socage, sock, soggy, soke, soma, some, soy, soya, syce, syke, ya, yack, yacks, yagi, yagis, yak, yaks, yam, yams, ye, yea, yeas, yegg, yeggs, yes, yikes, yock, yocks, yoga, yogas, yogi, yogic, yogis, yoicks, yok, yoke, yokes, yoks, yom'
f=e.split(', ')
"Hey you! There's a puzzle in here. Click on the arrow for more clues.", 
			"This is a coding puzzle. You'll need to write some code.",
			"It isn't tough. The clues are all here, in this page",
			"But you'll have to look closely.",
			"It might not even be in these sentences.",
			"Look under the covers, as any good detective would",
			"Once you get the secret phrase, type it in the box to the left",
			"Who are we? We are the makers of <b>MakkhiChoose</b>",
			"If you haven't tried "+makkhi_link+", please do!",
			"The best way to save while shopping online, according to more than "+econ_link,
			"<b>You</b> can help us make it better, if you are good enough to crack this puzzle",
			"OK, that's all the help you'll get. Good luck!"
