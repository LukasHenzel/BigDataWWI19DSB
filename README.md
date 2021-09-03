# BigDataWWI19DSB
Big Data Gruppenaufgabe 
 
Matrikelnummern:
Lukas Henzel			2539341
Anne-Sophie Amberger	7053036
Niklas Lukas			5523187
Ann-Kathrin Kälberer		5799502
Marc Franke			9408418

Doku:

Das Big Data Projekt befasst sich vor allem mit der Entwicklung und dem Aufbau einer Big Data App. Diese soll hierbei in Echtzeit Datenabfragen durchführen, diese entsprechend verarbeiten und Speichern und in einer vor definierten Form einem Endnutzer zur Verfügung stellen.
Ziel ist es hierbei vor allem diesen Prozess so umzusetzen, dass er zum einen funktioniert und zum anderen auch alle wichtigen Komponenten enthält. Die Datenquantität und Komplexität sind dabei nicht so sehr entscheidend, da vor allem das Konzept der Anwendung im Vordergrund steht. Dies soll mit einem entsprechendem Use Case umgesetzt werden.
 
Der Use Case, für welchen sich die Gruppe entschieden hat, besteht darin, tagesaktuelle Coronazahlen nach Land darzustellen. Der Grund sich für eben diesen zu entscheiden, führte vor allem daher, da Corona ein sehr aktuelles Thema ist und die Menschen täglich beschäftigt. Somit ist es auch gut möglich passende Daten beziehungsweise eine verlässliche Datenquelle zu finden.
 
Hierfür werden nun die Daten 7 Tage gespeichert und mittels der in den Daten enthaltenen Popdata wird eine 7-Tages-Inzidenz berechnet.
Diese Werte zu Corona, sprich der neueste Fall, Todes- und Inzidenzzahlen, sollen nun in Form einer Tabelle pro Land abgebildet werden. 
 
Die von der Gruppe eingesetzten Prequesits sind nun folgende:  skaffold, docker, helm und minikube. Sie dienen vor allem dazu gemeinsam an der Applikation zu arbeiten und diese letztendlich auch einzusetzen (skaffold). Auch Docker bringt nun den Vorteil, dass es die einzelnen Bestandteile der Anwendung voneinander isoliert und ebenfalls in Container darstellt. Gleichzeitig wird minikube dafür verwendet ein lokales Kubernetes Cluster zu implementieren.  Zu guter Letzt ist helm dafür zuständig, eben dieses zu administrieren und zu verwalten. Das Kubernetes Cluster selbst wird wiederum benötigt, um entsprechend mit den einzelnen Containern der Datenbank zu arbeiten.
 
Denn eben der Data Lake wird durch Hadoop umgesetzt und managet diesen in unterschiedliche Container, um den Zugriff parallelisieren zu können und somit die Leistung bei Abfragen und Berechnungen zu erhöhen.
 
Wie bereits beschrieben, wird als Datenspeicher der Anwendung Apache Hadoop genutzt, welches im Hintergrund agiert. Diese Datenbank basiert hierbei auf postgre SQL. Für Speicherungen in der Datenbank sowie für Echtzeitabfragen dient Apache Spark. Dieses fragt somit die neusten Daten von dem European Centre for Disease Prevention and Control auf der Seite "https://www.ecdc.europa.eu/en/publications-data/data-daily-new-cases-covid-19-eueea-country" ab.
 
Für die Berechnung der 7-Tages-Inzidenz läuft im Hintergrund nun ein Kafka Cluster im Zusammenspiel mit nginx, welche die entsprechenden Zahlen auf Basis der Hadoop-Datenbank ermitteln. Letzteres soll hierbei als Loadbalancer dafür sorgen, dass die Berechnungslast auf allen Clustern gleich verteilt ist, um eine maximale Effizienz zu gewährleisten.
Eben diese 7-Tages-Inzidenz wird mithilfe der Summe der Cases der vergangenen Woche sowie der popData der entsprechenden Länder berechnet.
 
Auf all diesen wird eine Webapplikation mittels Flask gebaut, welche das Dashboard schlussendlich für den End-User abbildet. Dabei wird auch ein Cache eingesetzt, damit die Daten für eine kurze Zeit geladen bleiben, um unnötige "Abfragen" zu vermeiden und Berechnungen einzusparen.
 
 
Die größte Komplikation für die Gruppe war hierbei Kafka selbst. Sowohl die allgemeine Implementierung, um dieses aufzusetzen, als auch die Kommunikation von diesem mit den anderen Komponenten. So landeten die entsprechenden Pods regelmäßig in einem Crash-Loop-Backoff. Nach langem Überlegen und Ausprobieren schaffte man es jedoch, dies zu bewältigen und Kafka entsprechend aufzusetzen.
Darüber hinaus brachte auch bei dem Import von Python in Spark seine Schwierigkeiten mit sich. Diese konnte leider nicht gelöst werden, wodurch auch keine Daten für die Webapplikation bereitstanden.
 
Zusammenfassend kann man also festhalten, dass das Big Data Projekt und die damit verbunden Entwicklung eines Coronadashboardes verschiedenste Herausforderungen für die Gruppe beinhaltete. Diese kam vor allem durch die vielen verschiedenen Systemmodule, welche man nutzen musste, zustande. Jedoch waren sie auch notwendig, um alle Anforderungen entsprechend umsetzen zu können und man konnte auch allen Herausforderungen trotzen und die damit verbundene Probleme lösen.

