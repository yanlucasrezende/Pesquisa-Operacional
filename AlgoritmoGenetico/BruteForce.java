package AlgoritmoGenetico;

//Resolvendo o problema do Knapsack por forca bruta, enunciado no arquivo byHand.txt
public class BruteForce {

    private static final int MAX_WEIGHT = 14;
    private static final int[] BENEFIT_ARRAY = { 10, 6, 11, 6, 9 };
    private static final int[] COST_ARRAY = { 4, 2, 6, 3, 5 };
    private static final int[] VALUES = { 0, 1 };
    private static Resultado RES_FINAL = new Resultado();

    public static void main(String[] args) {

        for (int valP1 : VALUES) {
            for (int valP2 : VALUES) {
                for (int valP3 : VALUES) {
                    for (int valP4 : VALUES) {
                        for (int valP5 : VALUES) {
                            Resultado resul = new Resultado();

                            int[] escolha = { valP1, valP2, valP3, valP4, valP5 };

                            resul.setEscolha(escolha);

                            if (RES_FINAL.getBeneficio() < resul.getBeneficio() && resul.getCusto() <= MAX_WEIGHT) {
                                RES_FINAL = resul;
                            }
                        }
                    }
                }
            }
        }

        System.out.println("## MELHOR ESCOLHA POSSIVEL ##");
        System.out.println("Item 1: " + (RES_FINAL.getEscolha()[0] == 1 ? "SIM" : "NAO"));
        System.out.println("Item 2: " + (RES_FINAL.getEscolha()[1] == 1 ? "SIM" : "NAO"));
        System.out.println("Item 3: " + (RES_FINAL.getEscolha()[2] == 1 ? "SIM" : "NAO"));
        System.out.println("Item 4: " + (RES_FINAL.getEscolha()[3] == 1 ? "SIM" : "NAO"));
        System.out.println("Item 5: " + (RES_FINAL.getEscolha()[4] == 1 ? "SIM" : "NAO"));
        System.out.println("Lucro de: " + RES_FINAL.getBeneficio() + ", e peso de: " + RES_FINAL.getCusto());

    }

    private static int calcularBeneficio(int[] escolha) {
        int benefit = 0;
        for (int i = 0; i < 5; i++) {
            if (escolha[i] == 1) {
                benefit += BENEFIT_ARRAY[i];
            }
        }
        return benefit;
    }

    private static int calcularCusto(int[] escolha) {
        int custo = 0;
        for (int i = 0; i < 5; i++) {
            if (escolha[i] == 1) {
                custo += COST_ARRAY[i];
            }
        }
        return custo;
    }

    public static class Resultado {
        private int beneficio = 0;
        private int custo = 0;
        private int[] escolha = { 0, 0, 0, 0, 0 };

        public int getBeneficio() {
            return beneficio;
        }

        public int getCusto() {
            return custo;
        }

        public int[] getEscolha() {
            return escolha;
        }

        public void setEscolha(int[] escolha) {
            this.beneficio = calcularBeneficio(escolha);
            this.custo = calcularCusto(escolha);
            this.escolha = escolha;
        }
    }
}
