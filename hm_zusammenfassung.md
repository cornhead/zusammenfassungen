---
title: "**Zusammenfassung: Hardware Modelling**"
...

---

An dieser Zusammenfassung kann gerne auf [Github](https://github.com/cornhead/zusammenfassungen.git) mitgewirkt werden!

---


# Hardware Design

Wann eine Hardware-Implementierung sinnvoll ist:

* wenn Off-the-shelf-Hardware die Erfordernisse nicht erfüllt (Performance, Effizienz, Sicherheit, Größe)
* wenn lange Entwicklungszeiten und hohe Kosten toleriert werden können
* wenn der mögliche Gewinn die Kosten übersteigt



Table: Hardware vs. Software

------------------------------------------------------
             &nbsp;    Hardware         Software      
-------------------    --------         --------      
         Ausführung    gleichzeitig     sequentiell

       Aktive Teile    alle             nur verwendete
                                        Code-Zeile
      
 Mehr Instruktionen    mehr Hardware    mehr Rechenzeit
       führen zu...
      
  Begrenzende Größe    Fläche           Zeit
-------------------------------------------------------


## Hardwarebeschreibungssprachen (HDLs)

HDLs auf dem Y-Diagramm:

* meistens auf der RTL- oder Logic-Ebene des Y-Diagramms (siehe VO Digital Design)
* meistens auf der Verhaltens- oder Strukturachse des Y-Diagramms
* in seltenen Fällen auch auf algorithmischer Ebene
* tieferliegende Ebenen werden durch Tools realisiert

Aufgaben von HDLs:

* höhere Abstraktion &rarr; geringere Produktivitätslücke
* Dokumentation (ursprünglicher Zweck von VHDL)
* Kommunikation

Produktivitäts-/Verifikations-Lücke:

1. Durch bessere Technologie könnten immer mehr Gatter auf einen Chip passen
2. Es können aber nur begrenzt komplexe Schaltungen entworfen werden
3. und nur noch weniger komplexe Schaltungen verifiziert werden

Der Unterschied zwischen (1) und (2) ist die Produktivitätslücke, der Unterschied zwischen (1) und (3) die Verifikationslücke.



# VHDL

Um die zunehmende Komplexität von integrierten Schaltugen zu bewältigen, wird eine Beschreibung auf abstrakter/logischer
Ebene (ähnlich wie bei Software) notwendig. Zu diesem Zweck wurden Hardware-Beschreibungs-Sprachen (HDL) wie VHDL oder 
Verilog entwickelt. Dieser Kurs beschäftigt sich (Stand 2021) ausschließlich mit VHDL. 

Bei dieser Art der Entwicklung reicht es wenn lediglich die Funktionsweise des Schaltkreises beschrieben wird.
Es wird also das "Was" beschrieben. Das "Wie" also die konkrete Implementierung in physikalischer Hardware wird dem 
Synthese-Tool überlassen (z.B. Questa). Im Bereich der Hardware-Modellierung muss bei der Entwicklung unglücklicherweise 
diese Abstraktion hin und wieder aufgebrochen werden, um das Synthese-Tool zu unterstützen und auch die Hardware zu erhalten, die 
gewünscht ist. 

## VHDL-Sprachkonzepte

In VHDL wird das Design über Entities aufgebaut. Eine `entity` ist ein Funktionsblock der eine gewisse Aufgabe im Design 
übernimmt. Eine Entity kann zum Beispiel ein Synchronizer oder ein Parity-Erzeuger sein. Theoretisch kann das gesamte 
Design auch in einer einzelnen Entity gelöst werden. Von dieser Vorgehensweise wird aufgrund von schlechter 
Wartbarkeit/Skalierbarkeit abgeraten.

**Deklaration einer Entity**

Eine Entity wird wie folgt in einem VHDL-File (.vhd-Extension) deklariert.

```
entity <entity-name> is 
port 
( 
       <first-input-signal> : in STD_LOGIC; 
       <second-input-signal> : in STD_LOGIC; 
       
       <first-output-signal> : out STD_LOGIC; 
       <second-output-signal> : out STD_LOGIC; 
       <third-output-signal> : out STDL_LOGIC
);
```

Die Ausdrücke(Identifier) in den Spitzklammern z.B. <entity-name> können beliebig vom Designer gewählt werden.
Als Entity-Name kann beispielsweise `sync` für Synchronizer vergeben werden. 

Die Deklaration einer Entity beginnt mit dem Entity-Name, gefolgt von der Port-Map. Die Port-Map definiert die Schnittstelle
zum restlichen Design. Unser Beispiel hat zwei Eingangs- und drei Ausgangssignale. Diese sind am Schlüsselwort `in` bzw `out`
erkennbar. Es gibt auch Signale die gelesen und geschrieben werden können. Diese werden mit `inout` deklariert. Es 
gibt auch noch weitere Port-Modes die in kleineren Designs nicht allzu häufig zur Anwendung kommen (vgl `linkage` und `buffer`).

Damit wäre die Schnittstelle der Entity definiert. Jetzt fehlt noch die tatsächliche Logig der Entity. Das
wird über eine `architecture` implementiert. 

**Deklaration einer Architecture**

Eine Architecture wird üblicherweise im gleichen VHDL-File wie die Entity deklariert.

```
architecture <architecture-name> of <entity-name> is
begin 
       <logic> 
end architecture; 
```

Hierbei kann der Architekturname frei gewählt werden. Der Entity-Name muss der selbe wie bei der Entity-Deklaration sein. 

**Beispiel: Multiplexer in VHDL**

```
entity MUX21 is 
port 
( 
       I0, I1, S : in STD_LOGIC; 
       0 : in STD_LOGIC
);

architecture muxlogic of MUX21 is
begin 
       O <= (I0 and (not S)) or (I1 and S)
end architecture; 
```

Signale werden über den Pfeiloperator `<=` zugewiesen. 

**Anmerkung zu Identifiers**

Ein Identifier (z.B. Namer einer Entity, Signals oder Architektur) hat gewisse Einschränkungen in VHDL. 

* Das erste Zeichen muss ein Buchstabe sein 
* Das letzte Zeichen darf kein Unterstrich sein 
* Es dürfen keine zwei Unterstriche aufeinanderfolgen

## VHDL-Sprachmittel

Bisweilen wurde nur einzelne Signal-Zuweisung mittels Boolscher-Operatoren betrachtet. Bei komplexerer Logik 
wird diese aber auch schnell unübersichtlich. VHDL bietet einige Sprachmittel, um dies übersichtlicher zu gestalten. 

**Interne Signale**

Wir betrachten folgende Architektur: 

```
architecture muxlogic of MUX21 is
begin 
       O <= (I0 and (not S)) or (I1 and S)
end architecture; 
```
Diese kann auch geschrieben werden als: 

```
architecture muxlogic of MUX21 is
 signal A0, A1: STD_LOGIC;
begin 
       A0 <= (I0 and (not S))
       A1 <= (I1 and S)
       O <= A0 or A1
end architecture; 
```

Signale die nicht über die Entity hinweg propagiert werden sollen, werden innerhalb der Architektur definiert.
In Hardware kann man sich die Signale auch als benannte Leitungen (named wires) vorstellen. In diesem Fall geben wir den beiden 
Leitungen (Wires), die zum `or`führen einen expliziten Namen.

**Vektordatentypen**

Bis jetzt wurden nur Signale mit einer Breite von einem Bit verwendet. Um einen breiteren Datenbus zu implementieren, 
müssen nicht manuell `n`-neue Signale bzw. Ports angelegt werden. 

```
entity MUX41 is 
port 
( 
       I0, I1, I2, I3 : in STD_LOGIC; 
       S : in STD_LOGIC_VECTOR(1 downto 0);
       0 : in STD_LOGIC
);
```

Hier sehen wir einen Multiplexer der aus vier Eingängen einen Ausgang auswählt. Dazu benötigen wir 2-Bit für
das Select-Signal. Dieses definieren wir als STD_LOGIC_VECTOR mit einer Breite von 2 Bit. 

Eine Entity mit einem Eingangsdatenbus von 8-Bit würde beispielsweise so aussehen: 

```
entity Example is 
port 
( 
       I : in STD_LOGIC_VECTOR(7 downto 0); 
       0 : in STD_LOGIC
);
```

**Konditionelle Zuweisung**

Es ist auch möglich Fallunterscheidung bei der Signal-Zuweisung durchzuführen. Das geht mit dem `conditional` oder 
`selected`-Statement.

Zuweisung mit `conditional`. Hier wieder der 4-1 Mux als Beispiel.

```
architecture conditional of MUX41 is
begin
       O <= I0 when S="00" else
            I1 when S="01" else
            I2 when S="10" else
            I3;
end architecture;
```

Zuweisung mit `selected`. Gleiches Beispiel.

```
architecture conditional of MUX41 is
begin
       with S select
       O <= I0 when "00",
            I1 when "01",
            I2 when "10",
            I3 when others;
end architecture;
```

Selected wählt aus einem Signal aus wohingegen die Conditional-Anweisung Boolsche-Ausdrücke evaluiert. Im Selected-
Beispiel wird auch das Vektor-Literal verwendet. Ein Vektor kann in VHDL bequem über die Doppelhochkomma verglichen 
werden. 

**Generics**

Um seine Entity vielseitiger einzusetzen, ist es auch möglich gewisse Werte vom Verwender der Entity definieren zu lassen. 
So kann z.B. ein Multiplexer definiert werden, der eine variable Eingangs- und Ausgangsbreite hat. 

```
entity MUX41 is
generic ( width : NATURAL := 2);
port (
       I0, I1: in STD_LOGIC_VECTOR(width-1 downto 0);
       S : in STD_LOGIC;
       O : out STD_LOGIC_VECTOR(width-1 downto 0)
     );
end entity;
```

Generics werden in der Generic-Map zugewiesen. Genau so wie Signale haben sie einen Datentyp. Die Zuweisen `:= 2` im 
Beispiel ist ein Default-Wert. Dieser kommt zur Anwendung, wenn der Verwender der Entity das Generic nicht setzt.

## Entity-Verknüpfung (Structural Design)

Es wurde bereits diskutiert, dass sich ein Design aus mehreren Entities zusammensetzt. Noch ist nicht klar wie
dies in VHDL realisiert werden kann. 

Dazu werden zunächst drei Begriffe: 

* Component Declaration 
* Component Instantiation 
* Component Configuration

**Component Declaration**

Um eine Entity innerhalb einer anderen Entity zu verwenden, wird als erstes eine Component Declaration benötigt. 

```
component MUX41Comp is
generic ( width : NATURAL );
port (
       I0, I1: in STD_LOGIC_VECTOR(width-1 downto 0);
       S : in STD_LOGIC;
       O : out STD_LOGIC_VECTOR(width-1 downto 0)
     );
end entity;
```

Eine Komponente hat in etwa den gleichen Aufbau, wie eine Entity. Die Komponente definiert die Schnittstelle zu 
der Entity, die verwendet werden soll. Für unsere Zwecke genügt es meist, die Entity zu kopieren. 
Component-Declaration können sich entweder in Paketen oder am Beginn einer Architecture befinden.

**Component Instantiation**

Die Component Instantiation verknüpft die Komponente mit unserem Design. 

```
architecture ...
       component ...
       signal TB_I0, TB_I1, TB_S, TB_O, ...
begin   
       ...
       COMP_INST: MUX41Comp
       generic map (width => 2) 
       port map(
              I0 => TB_I0, 
              I1 => TB_I1, 
              S => TB_S, 
              O => TB_O
       );

end architecture;    
```

Hier werden in unserer Architecture die Signale der Komponente mit unseren internen Signalen verbunden. 
Auf der linken Seite der Portmap stehen die Signale der Komponente. 

Achtung! Hier wird nur die Komponente mit unserem Design verknüpft. Es gibt noch keine Verbindung zu einer konkreten Entity.
Hierfür benötigt es die Component Configuration. 

**Component Configuration**

Die Component Configuration legt fest, welche Entity mit welcher Architecture in unsere Komponente gesetzt wird. Eine 
Entity kann nämlich auch über mehrere Architekturen verfügen. 

```
configuration v1 of testbench is
 for beh
       for SEL : MUX41Comp
              use entity MUX41(selected);
       end for;
       for COND : MUX41Comp
              use entity MUX41(concurrent);
       end for;
  end for;
end conguration v1;
```

Angenommen wir befinden uns in einer Architektur `beh` dort gibt es zwei Component Instantiations `SEL : MUX41Comp`
und `COND : MUX41Comp`. Nun wollen wir das die Komponente `SEL` mit unserer Selected-Implementierung des Multiplexer 
befüllt wird. Die Komponenten-Instanz mit dem Namen `Cond` sollt mit der Concurrent-Implementierung des Multiplexers 
befüllt werden. 

Hier werden zwei Komponenten-Instanzen mit der gleichen Entity aber unterschiedlichen Architektur befüllt. 
Auch ist es möglich das zwei Instanzen der gleichen Komponente mit unterschiedlichen Entities befüllt werden. 

Die Component Configuration **kann weggelassen werden**, falls Entity und Archtiektur im Design eindeutig sind.

# Hardware Modelling
