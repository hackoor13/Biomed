Had lprojet fih code dyal Biomed ,hna drt code dyal 2D oli t9dr tkhtar fih lblays li mnin imkn idkhol oxygen 

KIFACH TKHDMO HADCHI:

1. Awl haja khas ykon 3ndkom Git installé.
   Ila ktbto:
   git --version
   w 3takom version, sf kolchi mzyan.

2. Mchiw l CMD dyalkom awla terminal dyal VS Code.
3. Ktbo:
git clone https://github.com/hackoor13/Biomed.git
(Ila bghito tcolliw f terminal: Ctrl + Shift + V)

4. Moraha ktbo:
cd Biomed
Daba khas tl9aw files kamlin tma.
T9dro tbddlo lcode kifma bghito f PC dyalkom,
w dakchi li katbdlo ma kay2atrch 3la version li 3ndi f GitHub.

5. Ila drt ana chi update wla zdt chi haja,
dkhlo l folder Biomed w diro:

git pull

w ayjib likom akhir version.

IMPORTANT:
Mat3awdouch diro git clone kol mara.
git clone katdiroha ghir awl mara.
Moraha ghir git pull bach tjibo updates.

la7tajito chi haja sifto mail f khalildriyer@gmail.com

## Install the required libraries
khdmt bnumpy omatplotlib donc tantoma khas ykono 3ndkom ohit ana adka wahd femines shlt 3likom l9adiya 
atmchi lcmd mra akhra o tktbo : pip install -r requirements.txt (okhas diro hadchi wst Biomed z3ma fcmd tkon mktoba chi haja /Biomed) (lam3rftoch diro cd Biomed bhal 9bila)



Chkadir M li flcode:

had M hiya fin kaynin dok lblays li kaydkhl menhom O2 donc matalan la bghiti tkon jiha lisriya kamla kaydkhl menha O2 dir M =[i for i in range(Ny)],bghiti ghir pixel li lwst li idkhl meno O2 adir M = [Ny//2]


ah o lblays li mafihomch door (lblasa li makaydkhlch menha O2) rah drthom kayverifiw lcondition du/dn = 0 ki b7al les bornes li lfo9 olt7t
