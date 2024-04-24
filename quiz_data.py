class QuizData:
    def __init__(self):
        self.quiz_dict = {
            "메시지 Checksum을 활용한 데이터 인증과 비연결형 무결성을 보장해주는 프로토콜": "AH",
            "암호화 알고리즘을 활용한 캡슐화 기반 페이로드 기밀성을 제공하는 프로토콜": "ESP",
            "업무중단 시점부터 업무가 복구되어 다시 가동될 때까지의 시간": "RTO",
            "DRS의 유형으로 데이터만 원격지에 보관하고, \
재해 시 데이터를 근간으로 필요 자원을 조달하여 복구할 수 있는 재해복구센터로 \
재해 발생 시 복구까지의 소요 시간은 수주에서 수개월이 걸린다.": "Cold Site",
            "가장 간단한 구조를 가지며, \
평문을 일정한 블록 단위로 나누어 순차적으로 암호화하는 구조 \
모든 블록이 같은 암호화 키를 사용하기 때문에 \
보안에 취약하고 특히 반복공격에 취약": "ECB",
            "웹상에 존재하는 데이터를 개별 URI로 식별하고, \
각 URI에 링크 정보를 부여함으로써 상호 연결된 웹을 지향하는 아키텍처": "LOD",
            "작성해야 하는 프로그램에 대한 테스트를 먼저 수행하고 \
이 테스트를 통과할 수 있도록 실제 프로그램의 코드를 작성한다는 원리": "TDD",
            "정보시스템 개발에 필요한 관리 절차와 작업 기반을 체계화한 방법론으로\
 대형 프로젝트를 수행하는 체계적인 방법론": "Information Engineering Development",
            "특정 제품에 적용하고 싶은 공통된 기능을 정의하여 개발하는 방법론으로 \
임베디드 소프트웨어를 작성하는 데 유용한 방법론": "Product Line Development",
"전송계층과 응용계층 사이에서 클라이언트와 서버 간의 웹 데이터 암호화(기밀성), 상호인증 및 \
전송 시 데이터 무결성을 보장하는 보안 프로토콜로 Https://~ 표시형식과 443 포트를 이용":"SSL",
"웹상에서 네트워크 트래픽을 암호화하는 주요 방법 중 하나로 클라이언트와 서버 간에 전송되는 모든 메시지를 암호화해서 전송한다. \
메시지 보호는 HTTP를 사용한 애플리케이션에 대해서만 가능하다.":"S-HTTP",
"유한체 위에서 정의된 타원곡선 군에서의 이산대수 문제에 기초한 암호화 알고리즘으로 \
RSA보다 키의 비트 수를 적게하면서 동일한 성능을 제공하는 비대칭키 암호화 알고리즘":"ECC",
"TCP/IP의 네트워크 관리 프로토콜로, 라우터나 허브 등 네트워크 장치로부터 정보를 수집 및 관리하며, \
정보를 네트워크 관리 시스템에 보내는 데 사용되는 인터넷 표준 프로토콜. \
UDP 161번 포트와 UDP 162번 포트를 사용":"SNMP",
"2개 이상의 스위치가 여러 경로로 연결될 때, 무한 루프 현상을 막기 위해서 우선순위에 따라 1개의 경로로만 통신하도록 하는 프로토콜":"STP",
"IEEE 802.11i에서 정의한 무선 랜 암호화 방식으로 임시키 무결성 프로토콜, 메시지의 무결성 코드(MIC)와 RC4 암호 알고리즘을 이용하여 메시지의 무결성과 데이터 기밀성을 제공":"TKIP",
"AES를 기반으로 한 IEEE 802.11i 암호화 프로토콜로 높은 보안성 패킷의 데이터 영역과 IEEE 802.11 헤더의 무결성을 보장하고 패킷 번호를 이용하여 재전송 공격을 방지하는 프로토콜":"CCMP",
"일의 순서를 계획적으로 정리하기 위한 수렴기법으로 비관치, 중간치, 낙관치의 3점 추정방식을 통해 일정 관리":"PERT",
"시스템이 어떤 기능을 수행하는지를 객체의 처리 로직이나 조건에 따른 처리의 흐름을 순서대로 표현하는 다이어그램":"Activity Diagram",
"동작에 참여하는 객체들이 주고 받는 메시지를 표현하고, 메시지뿐만 아니라 객체 간의 연관까지 표현하는 다이어그램":"Communication Diagram",
"소프트웨어 아키텍처 4+1 뷰 중 시스템의 비기능적인 속성으로서 자원의 효율적인 사용, 병행 실행, 비동기, 이벤트 처리 등을 표현한 뷰로 개발자, 시스템 통합자 관점의 뷰":"Process View",
"객체의 전이를 유발하는 자극으로 상태의 변화를 주는 현상":"Event",
"특정 조건 만족 시 전이 발생하도록 하기 위해 사용되는 속성값들의 불리언 식":"전이 조건",
"보안 취약점이 발견되어 널리 공표되기 전에 해당 취약점을 악용하여 이루어지는 보안 공격기법으로 이전에 알려지지 않은 취약성을 이용하는 사이버 공격":"Zero Day Attack",
"컴포넌트가 물리적인 아키텍처에 어떻게 배치되는가를 매핑해서 보여줌. 물리적인 시스템을 구성하고 있는 각 부분들의 분산 형태와 설치에 초점을 둠" : "Deployment View",
"일반적으로 스위치 장치는 MAC 주소 테이블이 가득 차게 되면 모든 네트워크 세그먼트로 트래픽을 브로드캐스팅하는 특성을 가지고 있다. \
이런 특성을 이용하여 공격자는 위조된 MAC 주소를 지속적으로 네트워크에 전송함으로써 스위칭 허브의 주소 테이블을 오버플로우시켜 허브처럼 동작하게 만든 후 다른 네트워크 세그먼트의 데이터를 스니핑한다.":"Switch Jamming",
"연산,통신,조정을 책임지는 부분과 제어되고 동기화되는 대상인 부분으로 구성되는 패턴, 슬레이브 컴포넌트에서 처리된 결과물을 다시 돌려받는 방식으로 작업을 수행하는 패턴":"Master-Slave",
"각 시스템 간에 공유 디스크를 중심으로 클러스터링으로 엮어 다수의 시스템을 동시에 연결, 조직,기업의 기간 업무 서버 등의 안정성을 높이기 위해 사용될 수 있다. 여러 가지 방식으로 구현되며 2개의 서버를 연결하는 것으로 2개의 시스템이 각각의 업무를 수행하도록 구현하는 방식이 널리 사용":"HACMP",
"메모리에 적재되어 있는 코드 조각들(가젯)에 Return 명령을 사용하여 공격자가 원하는 흐름대로 명령을 실행하도록 하는 공격기법, 버퍼 오버플로우와 같은 취약점을 이용하여 프로그램의 실행 흐름을 조작할 때 가장 빈번하게 사용":"ROP",
"PC가 악성코드에 감염되어 정상적인 홈페이지 주소를 입력하거나 기존에 설정해 둔 즐겨찾기로 접속해도 악성 사이트로 연결되어 개인의 금융정보를 훔치는 공격 기법":"Pharming",
"두 사용자 간에 공통의 암호키를 안전하게 공유할 방법을 제시하였으며, 키 분배 방식에 관한 연구의 기본":"Diffie-Hellman",
"소프트웨어 개발 과정에 대한 테스트이고 개발자 혹은 시험자의 시각으로 소프트웨어가 명세화된 기능을 올바로 수행하는지":"Verification",
"소프트웨어 결과에 대한 테스트이고 사용자의 시각으로 올바른 소프트웨어가 개발되었는지를 입증":"Validation",
"M2M 노드들 사이에서 이벤트에 대한 송수신을 비동기적으로 전송하는 REST 프로토콜이자 제약이 있는 장치들을 위한 특수한 인터넷 애플리케이션 프로토콜로 다양한 IoT 산업에서의 활용범위가 넓어지고 있다.":"COAP",
"네트워크를 경유하는 프로세스 간 통신의 접속점으로 클라이언트와 서버 프로그램 사이에 데이터를 송수신 할 수 있다. IP Address와 Port가 합쳐진, 네트워크 상에서 서버 프로그램과 클라이언트 프로그램이 통신할 수 있도록 해주는 교환 기술":"Socket",
"서비스 호출, 컴포넌트 재사용 등 다양한 환경을 지원하는 테스트 프레임워크로 각 테스트 대상 분산 환경에 데몬을 사용하여 테스트 대상 프로그램을 통해 테스트를 수행하고, 통합하여 자동화하는 검증도구":"STAF",
"토요타에서 처음 사용한 애자일 프로젝트 관리에 사용되는 시각화 도구로 전체 워크플로룰 카드 형태로 나타내고 수행된 활동, 진행중인 작업 및 보류중인 활동을 구별할 수 있는 도구":"Kanban Board",
"스프린트가 끝난 시점이나 일정 주기별로 스프린트 주기를 되돌아보며 정해놓은 규칙 준수 여부, 개선점 등을 확인하고 기록하는 과정":"Sprint Retrospective",
"DDos 공격자들은 trinoo와 거의 유사한 분산 도구로 많은 소스에서 하나 혹은 여러 개의 목표 시스템에 대해 서비스 거부 공격을 수행할 수 있는 도구인 (   )을 이용하여 간편하게 디도스 공격을 시도":"TFN",
"TFN과 같은 공격 도구를 통해 출발지 주소 공격 대상 서버의 IP로 설정하여 네트워크 전체에게 ICMP Echo 패킷을 직접 브로드캐스팅하여 마비시키는 공격":"Smurf",
"테스트 데이터 값들간에 최소한 한 번씩을 조합하는 방식이며, 이는 커버해야 할 기능적 범위를 모든 조합에 비해 상대적으로 적은 양으 테스트 세트를 구성하기 위한 테스트 기법":"pairwise Testing",
"ICMP 패킷(Ping)을 정상적인 크기보다 아주 크게 만들어 전송하면 다수의 IP 단편화가 발생하고, 수신 측에서는 단편화된 패킷을 처리(재조합)하는 과정에서 많은 부하가 발생하거나, 재조합 버퍼의 오버플로우가 발생하여 정상적인 서비스를 하지 못하도록 하는 공격기법":"Ping of Death",
"송수신 간의 논리적인 연결을 수행하고, 대표적인 프로토콜에는 RPC, NetBIOS가 있다.":"Session Layer",
"XP의 기본원리 중 공통적인 이름 체계와 시스템 서술서를 통해 고객과 개발자 간의 의사소통을 원활하게 한다는 원리":"메타포어",
"전문자의 경험적 지식을 통한 문제 해결 및 미래 예측을 위한 요구사항 도출 기법":"Delphi Method",
"웹 서비스에 대한 정보인 WSDL을 등록하고 검색하기 위한 저장소로 공개적으로 접근, 검색이 가능한 레지스트리이자 표준":"UDDI",
"실세계에 존재하는 모든 개념들과 개념들의 속성, 그리고 개념들 간의 관계 정보를 컴퓨터가 이해할 수 있도록 서술해 놓은 개념화 명세서":"Ontology",
"웹 기반 테스트 케이스 설계/실행/결과 확인 등을 지원하는 테스트 프레임워크로 사용자가 테스트 케이스 테이블을 작성하면 빠르고 편하게 자동으로 원하는 값에 대해 테스트를 할 수 있는 장점이 있다.":"FitNesse",
"네트워크에 대한 공격이나 침입을 실시간적으로 차단하고, 유해트래픽에 대한 조치를 능동적으로 처리하는 시스템":"IPS",
"모든 하드웨어가 가상화되어 가상 자원의 풀을 구성하고 데이터 센터 전체를 운영하는 소프트웨어가 필요한 기능 및 규모에 따라 자원을 할당, 관리하는 역할을 수행하는 데이터 센터":"SDDC",
"서버와 저장 장치를 네트워크로 연결하는 방식으로, 구성 설정이 간편하여 별도의 운영체제를 가진 서버 한 곳에서 파일을 관리하기 때문에 서버 간 스토리지 및 파일 공유가 용이한 스토리지 장치 구성 방식":"NAS",
"구체적인 클래스에 의존하지 않고, 인터페이스를 통해 서로 연관,의존하는 객체들의 그룹으로 생성하여 추상적으로 표현하는 패턴, 연관된 서브 클래스를 묶어 한 번에 교체하는 것이 가능":"Abstract Factory",
"작게 분리된 인스턴스를 건축하듯이 조합하여 객체를 생성하는 패턴, 객체의 생성 과정과 표현 방법을 분리하고 있어, 동일한 객체 생성에서도 서로 다른 결과를 만들어낼 수 있다.":"Builder",
"객체 생성을 서브 클래스에서 처리하도록 분리하여 캡슐화한 패턴, 상위 클래스에서 인터페이스만 정의하고 실세 생성은 서브 클래스가 담당, 가상 생성자(Virtual Constructor)패턴 이라고도 한다.":"Factory Method",
"원본 객체를 복제하는 방법으로 객체를 생성하는 패턴,  일반적인 방법으로 객체를 생성하며 비용이 큰 경우 주로 이용":"Prototype",
"하나의 객체를 생성하면 생성된 객체를 어디서든 참조할 수 있지만, 여러 프로세스가 동시에 참조할 수는 없는 패턴, 클래스 내에서 인스턴스가 하나뿐임을 보장하며, 불필요한 메모리의 낭비를 최소화 할 수 있다.":"Singleton",
"호환성이 없는 클래스들의 인터페이스를 다른 클래스가 이용할 수 있도록 변환해주는 패턴, 기존의 클래스를 이용하고 싶지만 인터페이스가 일치하지 않을 때 이용":"Adapter",
"구현부에서 추상층을 분리하여 서로가 독립적으로 확장할 수 있도록 구성한 패턴, 기능과 구현을 두 개의 별도 클래스로 구현":"Bridge",
"여러 객체를 가진 복합 객체와 단일 객체를 구분 없이 다루고자 할 때 사용하는 패턴, 객체들을 트리 구조로 구성하여 디렉터리 안에 디렉터리가 있듯이 복합 객체 안에 복합 객체가 포함되는 구조를 구현":"Composite",
"객체 간의 결합을 통해 능동적으로 기능들을 확장할 수 있는 패턴, 임의의 객체에 부가적인 기능을 추가하기 위해 다른 객체들을 덧붙이는 방식으로 구현":"decorator",
"복잡한 서브 클래스들을 피해 더 상위에 인터페이스를 구성함으로써 서브 클래스들의 기능을 간편하게 사용할 수 있도록 하는 패턴, 서브 클래스들 사이에 통합 인터페이스를 제공하는 Wrapper 객체 필요":"Facade",
"인스턴스가 필요할 때마다 매번 생성하는 것이 아니고 가능한 한 공유해서 사용함으로써 메모리를 절약하는 패턴, 다수의 유사 객체를 생성하거나 조작할 때 유용하게 사용":"Flyweight",
"복잡한 시스템을 개발하기 쉽도록 클래스나 객체들을 조합하는 패턴으로, 대리자라고도 불린다. 내부에서는 객체 간의 복잡한 관계를 단순하게 정리해주고, 외부에서는 객체의 세부적인 내용을 숨겨주는 역할을 수행":"Proxy",
"요청을 처리할 수 있는 객체가 둘 이상 존재하여 한 객체가 처리하지 못하면 다음 객체로 넘어가는 형태, 요청을 처리할 수 있는 각 객체들이 고리로 묶여 있어 요청이 해결될 때까지 고리를 따라 책임이 넘어간다.":"Chain of Responsibility",
"요청을 객체의 형태로 캡슐화하여 재이용하거나 취소할 수 있도록 요청에 필요한 정보를 저장하거나 로그에 남기는 패턴, 요청에 사용되는 각종 명령어들을 추상 클래스와 구체 클래스로 분리하여 단순화":"Command",
"언어에 문법 표현을 정의하는 패턴, SQL이나 통신 프로토콜과 같은 것을 개발할 때 사용":"Interpreter",
"자료 구조와 같이 접근이 잦은 객체에 대해 동일한 인터페이스를 사용하도록 하는 패턴, 내부 표현 방법의 노출 없이 순차적인 접근이 가능":"iterator",
"수많은 객체들 간의 복잡한 상호작용을 캡슐화하여 객체로 정의하는 패턴, 객체 사이의 의존성을 줄여 결합도 감소":"Mediator",
"특정 시점에서의 객체 내부 상태를 객체화함으로써 이후 요청에 따라 객체를 해당 시점의 상태로 돌릴 수 있는 기능을 제공":"Memento",
"한 객체의 상태가 변화하면 객체에 상속되어 있는 다른 객체들에게 변화된 상태를 전달하는 패턴, 일대다의 의존성을 정의, 주로 분산된 시스템 간에 이벤트를 생성,발행하고 이를 수신해야 할 때 이용":"Observer",
"객체의 상태에 따라 동일한 동작을 다르게 처리해야 할 때 사용하는 패턴, 객체 상태를 캡슐화하고 이를 참조하는 방식으로 처리":"State",
"동일한 계열의 알고리즘들을 개별적으로 캡슐화하여 상호 교환할 수 있게 정의하는 패턴, 클라이언트는 독립적으로 원하는 알고리즘을 선택하여 사용할 수 있으며, 클라이언트에 영향 없이 알고리즘의 변경이 가능":"Strategy",
"상위 클래스에서 골격을 정의하고, 하위 클래스에서 세부 처리를 구체화하는 구조의 패턴, 유사한 서브 클래스를 묶어 공통된 내용을 상위 클래스에서 정의함으로써 코드의 양을 줄이고 유지보수를 용이하게 함":"Template Method",
"각 클래스들의 데이터 구조에서 처리 기능을 분리하여 클래스로 구성하는 패턴, 분리된 처리 기능은 각 클래스를 방문하여 수행":"Visitor"
        }

    def get_quiz_dict(self):
        return self.quiz_dict
