
public class Activity3 {
    // Earth year in seconds
    static final double EARTH_YEAR_SECONDS = 31557600;

    public static void main(String[] args) {
        // Given age in seconds
        double ageInSeconds = 1000000000;

        System.out.printf("Age on Earth: %.2f years%n", calculateAge(ageInSeconds, 1.37795));
        System.out.printf("Age on Mercury: %.2f years%n", calculateAge(ageInSeconds, 0.2408467));
        System.out.printf("Age on Venus: %.2f years%n", calculateAge(ageInSeconds, 0.61519726));
        System.out.printf("Age on Mars: %.2f years%n", calculateAge(ageInSeconds, 3.8806549));
        System.out.printf("Age on Jupiter: %.2f years%n", calculateAge(ageInSeconds, 13.862615));
        System.out.printf("Age on Saturn: %.2f years%n", calculateAge(ageInSeconds, 26.447498));
        System.out.printf("Age on Uranus: %.2f years%n", calculateAge(ageInSeconds, 95.016846));
        System.out.printf("Age on Neptune: %.2f years%n", calculateAge(ageInSeconds, 187.79132));
    }

    // Method to calculate age on a planet
    public static double calculateAge(double seconds, double orbitalPeriod) {
        double earthYears = seconds / EARTH_YEAR_SECONDS;
        return earthYears / orbitalPeriod;
    }
}
