public class Sistema {
    public static void run(){
        // Criação da conta
        Conta conta = new Conta("Ubiratan",
        "da Motta",
        "bira.motta",
        "email@gmail.com",
        "123.456.789-10",
        "01/01/2000",
        "+5511999999999");
        System.out.println(conta);

        // Adicionando redes sociais
        conta.addRedeSocial("bira_motta1609");
        conta.addRedeSocial("bira.motta");
        System.out.println(conta);
    }
}
