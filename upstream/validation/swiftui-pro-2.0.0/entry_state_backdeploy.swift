import SwiftUI
extension EnvironmentValues { @Entry var enabled: Bool = true }
struct Sample: View { @State private var count = 0; var body: some View { Text("\(count)") } }
